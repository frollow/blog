from posts.models import Post, Group
import random


def sidebar_context(request):
    all_posts = Post.objects.select_related("group", "author__user_profile").order_by(
        "-pub_date"
    )
    group_list = Group.objects.all()[:6]
    popular_list = list(all_posts[:3])
    random_post = random.choice(all_posts) if all_posts else None

    return {
        "popular_list": popular_list,
        "group_list": group_list,
        "random_post": random_post,
    }
