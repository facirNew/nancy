from django import template
from blog.models import *


register = template.Library()


@register.simple_tag()
def get_tags():
    return Tags.objects.all()


@register.inclusion_tag('blog/carusel.html')
def carusel():
    return
