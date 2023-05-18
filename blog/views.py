from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import AddPostForm, RegisterUserForm, LoginUserForm
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

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).prefetch_related('tags')


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
        return Blog.objects.filter(tags__slug=self.kwargs['tag_slug'], is_published=True).prefetch_related('tags')


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


class BlogSignIn(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/signin.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class BlogSignUp(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('home')


