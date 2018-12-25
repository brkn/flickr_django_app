from django.shortcuts import render
import requests
import json


def getPhotos(url=None, tags=['cat', 'dog'], tag_mode='all', page=None):
    if url:
        pass
    else:
        baseurl = "https://api.flickr.com/services/rest/?method=flickr.photos.search&format=json&nojsoncallback=1"
        api_key = '1ddb7df62cbdc4e07f6ec75ca78e2960'
        url = baseurl + "&api_key=" + api_key
        url += "&per_page=" + "20"
        url += "&sort=" + "interestingness-desc"
        url += "&media" + "photos"

        url += "&tag_mode" + tag_mode
        url += "&tags="
        for tag in tags:
            url += tag + ","
        url = url[:-1]

    if page:
        url += "&page=" + page
    response = requests.get(url).json()['photos']['photo']
    return response, url


def index(request):
    context = {}
    context['photos'], _ = getPhotos()
    return render(request, 'FlickrApp/index.html', context)
