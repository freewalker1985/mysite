from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def get_recent_post(num=3):
    return Post.published.all().order_by('publish')[:num]