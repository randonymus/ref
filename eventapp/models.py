from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import datetime

# Create your models here.


class Like(models.Model):
    liker = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    class Meta:
        unique_together = (
            ("liker", "content_type", "object_id"),
        )

    def __unicode__(self):
        return "%s likes %s" % (self.liker, self.content_object)


class Event(models.Model):
    EVENT_TYPES = (
                   (u'C', u'Course'),
                   (u'S', u'Seminar'),
                   (u'W', u'Workshop')
                   )
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    type = models.CharField(max_length=1, choices=EVENT_TYPES)
    subscribers = models.ManyToManyField(User, related_name='subscribers',
                                         blank=True)
    likes = generic.GenericRelation(Like)

    def __unicode__(self):
        return self.name


class News(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = generic.GenericRelation(Like)

    def __unicode__(self):
        return self.text
