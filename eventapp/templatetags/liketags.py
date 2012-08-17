from django import template

register = template.Library()


@register.simple_tag
def liketext(user, obj):
    return 'Like' if obj.likes.filter(liker=user).count() == 0 else 'Unlike'
