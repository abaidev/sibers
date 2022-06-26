from django.urls import path
from .views import PostListAPIView

app_name = 'news-api'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list')
]
