## urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.create_user),
    path('api/communities/', views.create_community),
    path('api/discussions/', views.create_discussion),
    path('api/comments/', views.create_comment),
]
