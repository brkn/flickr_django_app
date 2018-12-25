from django.shortcuts import render
import requests
import json

dummy = [
    {
        "id": "46438529361",
        "owner": "26982917@N02",
        "secret": "913c4e83d9",
        "server": "4910",
        "farm": 5,
        "title": "Porsche, 997 GT3RS, Wan Chai, Hong Kong",
        "ispublic": 1,
        "isfriend": 0,
        "isfamily": 0
    },
    {
        "id": "45525793405",
        "owner": "156824316@N05",
        "secret": "3e71c2185c",
        "server": "7874",
        "farm": 8,
        "title": "",
        "ispublic": 1,
        "isfriend": 0,
        "isfamily": 0
    }
]


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
    context = {
        # 'photos': dummy
    }
    context['photos'], _ = getPhotos()
    return render(request, 'FlickrApp/index.html', context)
