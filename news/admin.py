from django.contrib import admin
from .models import Post, Image


class ImagesStacked(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'id')
    search_fields = ('title',)
    inlines = [ImagesStacked]

