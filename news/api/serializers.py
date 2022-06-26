from rest_framework import serializers
from news.models import Post, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_images(self, obj):
        return ImageSerializer(instance=obj.image_set.all(), many=True).data
