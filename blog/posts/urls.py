from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("run-task/", views.run_task_now, name="run_task_now"),
    path('unlock/', views.unlock_tasks, name='unlock_tasks'),
    path("create/", views.post_create, name="create"),
    path("follow/", views.follow_index, name="follow_index"),
    path("group/<slug:slug>/", views.group_posts, name="group"),
    path("profile/<username>/", views.profile, name="profile"),
    path("<str:slug>/", views.post_detail, name="post_detail"),
    path("<str:slug>/edit/", views.post_edit, name="edit"),
    # path("<str:slug>/comment/", views.add_comment, name="add_comment"),
    path(
        "profile/<str:username>/follow/",
        views.profile_follow,
        name="profile_follow",
    ),
    path(
        "profile/<str:username>/unfollow/",
        views.profile_unfollow,
        name="profile_unfollow",
    ),
]
