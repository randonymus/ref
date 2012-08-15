from eventapp.models import Like, Event, News
from django.contrib import admin
from django.contrib.contenttypes import generic


class LikeInline(generic.GenericTabularInline):
    model = Like


class EventAdmin(admin.ModelAdmin):
    inlines = [
        LikeInline,
    ]


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        LikeInline,
    ]

admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Like)
