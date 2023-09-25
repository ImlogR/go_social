from django.urls import path
from .views import *


urlpatterns=[
    path('gen_users/', UserList.as_view(), name='user-list-generics')
]