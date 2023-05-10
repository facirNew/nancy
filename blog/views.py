from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import AddPostForm
from .models import *
from .utils import *


class BlogHome(DataMixin, ListView):
    model = Blog
    template_name = 'Blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class BlogContent(DataMixin, DetailView):
    model = Blog
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last'] = Blog.objects.all().reverse()[:5]
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class BlogTagSearch(DataMixin, ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Тег: ' + str(Tags.objects.get(slug=self.kwargs['tag_slug']).name))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs['tag_slug'], is_published=True)


class BlogAddPage(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/new_page.html'
    login_url = reverse_lazy('signin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создать пост')
        return dict(list(context.items()) + list(c_def.items()))


class BlogContact(DataMixin, ListView):
    model = Blog
    template_name = 'blog/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))


class BlogThank(DataMixin, ListView):
    model = Blog
    template_name = 'blog/thank.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Спасибо!')
        return dict(list(context.items()) + list(c_def.items()))


class BlogSignIn(DataMixin, ListView):
    model = Blog
    template_name = 'blog/signin.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация!')
        return dict(list(context.items()) + list(c_def.items()))


class BlogSignUp(DataMixin, ListView):
    template_name = 'blog/signup.html'
    model = Blog

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход!')
        return dict(list(context.items()) + list(c_def.items()))

