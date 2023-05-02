from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('content/<slug:post_slug>', BlogContent.as_view(), name='content'),
    path('contact/', contact, name='contact'),
    path('thank/', thank, name='thank'),
    path('base/', base),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('tag_search/<slug:tag_slug>', BlogTagSearch.as_view(), name='tag'),
    path('new_page/', AddPage.as_view(), name='addpage'),


]