
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.post, name="post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('following', views.following, name="following"),
    path("post/update/<int:post_id>/", views.update_post, name="update_post"),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
]
