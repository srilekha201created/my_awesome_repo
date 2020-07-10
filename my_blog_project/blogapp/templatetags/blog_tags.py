from django import template
from blogapp.models import Post
register=template.Library()


@register.simple_tag
def total_posts():#this is our own template so compulsory we required to register in template linrary
    return Post.objects.count()
@register.inclusion_tag('blogapp/latest_posts123.html') #return rendered template the response will be added to latest_post123.html
def show_latest_posts(count=5):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

from django.db.models import Count
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count] 
