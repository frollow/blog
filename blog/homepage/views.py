from django.shortcuts import render
from posts.models import Post


def index(request):
    all_posts = Post.objects.select_related("group", "author__user_profile").order_by(
        "-pub_date"
    )
    feature_list = all_posts[:4]
    latest_list = all_posts[4:9]

    context = {
        "feature_list": feature_list,
        "latest_list": latest_list,
    }
    return render(request, "homepage/main.html", context)
