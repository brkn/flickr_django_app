from django.shortcuts import render
import requests
import json
import re
from .models import RecentSearch


def getPhotos(url=None, tags=['kittens', 'puppies'], tag_mode='all', page=None):
    if url:
        pass  # TODO: fix here
    else:
        baseurl = "https://api.flickr.com/services/rest/?method=flickr.photos.search&format=json&nojsoncallback=1"
        api_key = '1ddb7df62cbdc4e07f6ec75ca78e2960'
        url = baseurl + "&api_key=" + api_key
        url += "&per_page=" + "20"
        url += "&sort=" + "relevance"
        url += "&media=" + "photos"

        url += "&tag_mode=" + tag_mode
        url += "&tags="
        for tag in tags:
            url += tag + ","
        url = url[:-1]

    if page:
        url += "&page=" + page
    response = requests.get(url).json()['photos']['photo']
    return response, url


def getWordsFromUserInput(input: str) -> list:
    input = re.sub(r'[\W_]', ' ', input)
    input = input.lower()
    return input.split()


def index(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        context['photos'], url = getPhotos()
    context['photos'] = [dict(
        photo, link=f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg") for photo in context['photos']]
    context['keywords'] = list(
        RecentSearch.objects.all().order_by('-date_entry').values())[:20]
    return render(request, 'FlickrApp/index.html', context)
