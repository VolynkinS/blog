from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='category'),
    # path('post/<str:slug>/', views.get_post, name='post'),
    path('post/<int:post_id>/', views.get_post, name='post'),
]
