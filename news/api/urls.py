from django.urls import path
from .views import PostListAPIView, PostSearchAPIView

app_name = 'news-api'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    path('search/<str:lookup>/', PostSearchAPIView.as_view(), name='post-search'),
]
