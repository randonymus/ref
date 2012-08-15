""" Eventapp views """

from django.shortcuts import render_to_response, get_object_or_404
from eventapp.models import Event, News, Like
from django.core.context_processors import csrf
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as django_logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType


def index(request):
    """ Index """
    likedobjs = lambda model: [like.content_object for like in
                        Like.objects.filter(liker=request.user,
                        content_type=ContentType.objects.get_for_model(model))]
    eventname = request.GET.get('eventname', '')
    res = {
             'news': News.objects.all(),
             'likednews': likedobjs(News),
             'events': Event.objects.filter(name__contains=eventname),
             'likedevents': likedobjs(Event),
             'eventname': eventname,
             'authed': request.user.is_authenticated(),
             'user': request.user
             }
    res.update(csrf(request))
    return render_to_response('templates/index.html', res)


@csrf_protect
@require_POST
@never_cache
def logout(request):
    """ CSRF-protected logout """
    django_logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))


@csrf_protect
@require_POST
@never_cache
@login_required
def like(request):
    """ Like """
    try:
        if request.POST['model'] == 'event':
            model = Event
        elif request.POST['model'] == 'news':
            model = News
        else:
            raise KeyError

        obj = get_object_or_404(model, id=request.POST['objid'])
        likeobj, created = Like.objects.get_or_create(
                         content_type=ContentType.objects.get_for_model(model),
                         object_id=obj.id,
                         liker=request.user
                           )
        if not created:
            likeobj.delete()
        return HttpResponseRedirect(reverse_lazy('index'))
    except KeyError:
        return HttpResponse('Bad request')


@csrf_protect
@require_POST
@never_cache
@login_required
def subscribe(request):
    """ Subscribe """
    try:
        event = get_object_or_404(Event, id=request.POST['eventid'])
        event.subscribers.add(request.user)
        event.save()
        return HttpResponseRedirect(reverse_lazy('index'))
    except KeyError:
        return HttpResponse('POST key missing: eventid')
