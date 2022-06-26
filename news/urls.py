from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.PostListView.as_view(), name='feed'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/search/', views.PostSearchView.as_view(), name='post-search'),
]
