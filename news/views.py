from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Post


class NewsListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/index.html'
    paginate_by = 1
    ordering = '-id'  # to avoid UnorderedObjectListWarning

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['paglim'] = self.request.session.get("paglim", default=self.paginate_by)
        return context

    def get_paginate_by(self, queryset):
        paginate_by_val = self.request.GET.get('paglim', default=self.paginate_by)
        return paginate_by_val

    def get(self, request, *args, **kwargs):
        request.session['paglim'] = self.request.GET.get('paglim', default=self.paginate_by)
        return super(NewsListView, self).get(request, *args, **kwargs)


def listing(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/index.html', {'posts': page_obj})
