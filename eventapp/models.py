from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    likers = models.ManyToManyField(User, related_name='likers', blank=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers',
                                         blank=True)

    def __unicode__(self):
        return self.name
