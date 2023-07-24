from django.shortcuts import render
from .models import Post, Category
from taggit.models import Tag
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
    paginate_by = 15

    def get_queryset(self):
        search = self.request.GET.get('query','')
        post_list = Post.objects.filter(
            Q(title__icontains = search)|
            Q(description__icontains = search)
        )
        return post_list

class PostDetail(DetailView):
    model = Post

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all().annotate(category_count = Count('post_category'))
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()[:4]
        return context
    
class PostByCategory(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']
        post_list = Post.objects.filter(
            Q(category__name__icontains = slug)
        )
        return post_list

class PostByTag(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']
        post_list = Post.objects.filter(
            Q(tags__name__icontains = slug)
        )
        return post_list