from django import template

register = template.Library()


@register.simple_tag
def liketext(user, obj):
    return 'Unlike' if obj.likes.filter(liker=user).exists() else 'Like'
