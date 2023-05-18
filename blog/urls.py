from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(BlogHome.as_view()), name='home'),
    path('content/<slug:post_slug>', cache_page(60)(BlogContent.as_view()), name='content'),
    path('contact/', BlogContact.as_view(), name='contact'),
    path('thank/', BlogThank.as_view(), name='thank'),
    path('signin/', BlogSignIn.as_view(), name='signin'),
    path('signup/', BlogSignUp.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
    path('tag_search/<slug:tag_slug>', cache_page(60)(BlogTagSearch.as_view()), name='tag'),
    path('new_page/', BlogAddPage.as_view(), name='addpage'),


]