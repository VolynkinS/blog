from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', views.ViewPost.as_view(), name='view_post'),
    path('tag/<str:slug>/', views.PostsByTag.as_view(), name='tag'),
    path('search/', views.Search.as_view(), name='search'),
]
