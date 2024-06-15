import logging

from celery_singleton import clear_locks
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from blog.celery import app as celery_app

from .forms import CommentForm, PostForm
from .models import Follow, Group, Post, User
from .tasks import fetch_and_create_post
from .utils import insert_advertisement

logger = logging.getLogger("posts")


def index(request):
    post_list = Post.objects.select_related("group").all()
    paginator = Paginator(post_list, settings.POSTS_FOR_PAGINATION)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, settings.POSTS_FOR_PAGINATION)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all().order_by("-pub_date")
    paginator = Paginator(post_list, settings.POSTS_FOR_PAGINATION)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    if request.user.is_authenticated:
        following = author.following.filter(user=request.user).exists()
    else:
        following = False
    context = {"author": author, "posts": posts, "following": following}
    return render(request, "posts/profile.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    related_posts = (
        Post.objects.filter(group=post.group)
        .select_related("group", "author__user_profile")
        .exclude(slug=slug)
        .order_by("-pub_date")[3:3]
    )
    comments = post.comments.all()
    sd = post.sd
    absolute_url = request.build_absolute_uri(
        reverse("posts:post_detail", args=[post.slug])
    )
    sd["mainEntityOfPage"] = absolute_url
    sd["url"] = absolute_url
    post.text = insert_advertisement(post.text, template="ads/post_detail.html")
    context = {
        "post": post,
        "form": form,
        "comments": comments,
        "related_posts": related_posts,
        "sd": sd,
    }
    return render(request, "posts/post_detail.html", context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, "posts/create_post.html", {"form": form})
    instance = form.save(commit=False)
    instance.author = request.user
    instance.save()
    return redirect("posts:profile", instance.author)


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author == request.user:
        form = PostForm(
            request.POST or None, files=request.FILES or None, instance=post
        )
        if not form.is_valid():
            context = {
                "form": form,
                "post": post,
                "is_edit": True,
            }
            return render(request, "posts/create_post.html", context)
        form.save()
    return redirect("posts:post_detail", slug)


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect("posts:post_detail", slug=slug)


@login_required
def follow_index(request):
    post_list = Post.objects.filter(author__following__user=request.user)
    paginator = Paginator(post_list, settings.POSTS_FOR_PAGINATION)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/follow.html", context)


@login_required
def profile_follow(request, username):
    following_author = get_object_or_404(User, username=username)
    if request.user == following_author:
        return redirect("posts:profile", username=username)
    Follow.objects.get_or_create(user=request.user, author=following_author)
    return redirect("posts:profile", username=username)


@login_required
def profile_unfollow(request, username):
    followed_author = get_object_or_404(User, username=username)
    Follow.objects.filter(user=request.user, author=followed_author).delete()
    return redirect("posts:profile", username=username)


def run_task_now(request):
    logger.debug("run_task_now view called")
    fetch_and_create_post.delay()
    logger.debug("Task fetch_and_create_post.delay() called")
    return JsonResponse({"status": "Task is running"})


def unlock_tasks(request):
    clear_locks(celery_app)
    return JsonResponse({"status": "All tasks unlocked"})


def generate_news_sitemap(request):
    recent_posts = Post.objects.filter(
        pub_date__gte=timezone.now() - timezone.timedelta(days=2)
    )
    posts_with_full_urls = [
        {
            "url": request.build_absolute_uri(post.get_absolute_url()),
            "pub_date": post.pub_date.strftime("%Y-%m-%d"),
            "title": post.title,
            "author_name": post.author.get_full_name(),
        }
        for post in recent_posts
    ]

    xml_content = render_to_string(
        "posts/sitemap/news_template.xml", {"posts": posts_with_full_urls}
    )
    return HttpResponse(xml_content, content_type="application/xml")
