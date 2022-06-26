from django.db.models import Q
from rest_framework.generics import ListAPIView
from .serializers import PostSerializer
from news.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostSearchAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        sf = self.kwargs.get('lookup')
        qs = Post.objects.filter(Q(title__icontains=sf))
        return qs
