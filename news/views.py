from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/index.html'
    paginate_by = 10
    ordering = '-id'  # to avoid UnorderedObjectListWarning

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['paglim'] = self.request.session.get("paglim", default=self.paginate_by)
        return context

    def get_paginate_by(self, queryset):
        paginate_by_val = self.request.GET.get('paglim', default=self.paginate_by)
        return paginate_by_val

    def get(self, request, *args, **kwargs):
        request.session['paglim'] = self.request.GET.get('paglim', default=self.paginate_by)
        return super(PostListView, self).get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
