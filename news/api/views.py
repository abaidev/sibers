from rest_framework.generics import ListAPIView
from .serializers import PostSerializer
from news.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
