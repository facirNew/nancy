from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .form import AddPostForm
from .models import *


class BlogHome(ListView):
    model = Blog
    template_name = 'Blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class BlogContent(DetailView):
    model = Blog
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Обратная связь'})


def thank(request):
    return render(request, 'blog/thank.html', {'title': 'Спасибо!'})


def base(request):
    return render(request, 'blog/base.html')


def signin(request):
    return render(request, 'blog/signin.html', {'title': 'Регистрация'})


def signup(request):
    return render(request, 'blog/signup.html', {'title': 'Вход'})


class BlogTagSearch(ListView):
    model = Blog
    template_name = 'Blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тег: ' + str(Tags.objects.get(slug=self.kwargs['tag_slug']).name)
        return context

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs['tag_slug'], is_published=True)


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/new_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать пост'
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, f'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(request, 'blog/new_page.html', {'title': 'Новый пост', 'form': form})