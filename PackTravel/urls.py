"""PackTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from user import views as userView
from search import views as searchViews
from publish import views as publishViews
from forum import views as forumViews
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", searchViews.search_index, name="search"),
    path("publish/", publishViews.publish_index, name="publish"),
    path("index/", userView.index, name="index"),
    path("", userView.index, name="index"),
    path("index/<username>", userView.index, name="index"),
    path("register/", userView.register, name="register"),
    path("logout/", userView.logout, name="logout"),
    path("login/", userView.login, name="login"),
    path("create_route/", publishViews.create_route, name="create_route"),
    path("update_route/<ride_id>", publishViews.update_route, name="update_route"),
    # path('add_route/', publishViews.add_route, name='add_route'),
    path("select_route/", publishViews.select_route, name="select_route"),
    path(
        "display_ride/<ride_id>",
        publishViews.display_ride,
        name="display_ride"),
    path("accounts/", include("allauth.urls")),
    path("logout/", LogoutView.as_view()),
    path("myrides/", userView.my_rides, name="myrides"),
    path("delete_ride/<ride_id>", userView.delete_ride, name="delete_ride"),
    path("update_route/<ride_id>", publishViews.update_route, name="update_route"),
    path("u/<userid>", userView.user_profile, name="user_profile"),
    path("edit-profile/", userView.edit_user, name="user_user"),
    path("forum/create_topic/", forumViews.create_topic, name="create_topic"),
    path(
        "forum/rides-with-topics/",
        forumViews.rides_with_topics,
        name="rides_with_topics",
    ),
    path(
        "forum/topics/<ride_id>/",
        forumViews.forum_topics,
        name="forum_topics"),
    path(
        "forum/topic/<topic_id>/",
        forumViews.forum_topic_details,
        name="forum_topic_details",
    ),
    path(
        "forum/add_comment/<topic_id>/",
        forumViews.add_comment,
        name="add_comment"),
    path(
        "packs-favorite/",
        publishViews.packs_favorite,
        name="packs_favorite"),
]
