from django.conf import settings
from django.shortcuts import render
from django.db.models import Q
from posts.models import Post
from .forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search_view(request):
    form = SearchForm(request.GET or None)
    context = {"form": form}

    if form.is_valid():
        query = form.cleaned_data.get("query")
        posts = (
            Post.objects.select_related("group", "author__user_profile")
            .filter(
                Q(title__icontains=query)
                | Q(short_text__icontains=query)
                | Q(text__icontains=query)
            )
            .distinct()
        )

        # Пагинация
        paginator = Paginator(posts, settings.POSTS_FOR_PAGINATION)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context["posts"] = posts
    return render(request, "search/search.html", context)
