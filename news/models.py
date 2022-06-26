from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post-detail', kwargs={'pk': self.pk})


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_query_name='images')
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads')
