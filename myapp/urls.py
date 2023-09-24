from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('like_post_via_profile', views.like_post_via_profile, name='like_post_via_profile'),
    path('upload', views.upload, name='upload'),
    path('post_upload_via_profile', views.post_upload_via_profile, name='post_upload_via_profile'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
    path('search', views.search, name='search')
]