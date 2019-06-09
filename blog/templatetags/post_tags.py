from django import template
from django.db.models.functions import ExtractMonth
from django.db.models.aggregates import Count, Sum
from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_post(num=3):
    return Post.published.all().order_by('publish')[:num]


@register.simple_tag
def archives():
    # guidang = Post.objects.values('created').annotate(Count('slug'))
    # return Post.objects.dates('created', 'month', order='DESC').values('created').annotate(count=Count('slug'))
    return Post.objects.dates('created', 'month', order='DESC')
    # import pdb; pdb.set_trace()


@register.simple_tag
def get_category():
    return Category.objects.all()


@register.simple_tag
def get_tags():
    return Tag.objects.all()