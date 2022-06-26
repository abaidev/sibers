from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from .models import Post, Image
from .forms import PostForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/index.html'
    paginate_by = 10
    ordering = '-id'  # to avoid UnorderedObjectListWarning

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['paglim'] = str(self.request.session.get("paglim", default=self.paginate_by))
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


class PostCreateView(CreateView):
    model = Post
    template_name = 'news/post_create.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        pf = self.form_class(request.POST)
        post_obj = pf.save()
        for image in request.FILES.getlist('images'):
            Image.objects.create(image=image, post=post_obj)
        return redirect(reverse('news:post-detail', kwargs={'pk':post_obj.id}))


class PostSearchView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/search_results.html'

    def get_queryset(self):
        sf = self.request.GET.get('lookup')
        qs = Post.objects.filter(Q(title__icontains=sf))
        return qs
