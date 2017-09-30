from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

def get_user(request, username):
    ratings = []

    user = get_object_or_404(User, username=username)
    for site in Site.__subclasses__():
        handle = getattr(user, site.__name__.lower())
        if(handle):
            try:
                rating = dict(site=site.__name__, info=site.objects.get(handle__iexact=handle))
                ratings.append(rating)
            except site.DoesNotExist:
                pass
    return render(request, 'rating/get_user.html', {'username': username, 'ratings': ratings})
