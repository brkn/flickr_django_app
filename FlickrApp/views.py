from django.shortcuts import render

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

def index(request):
    context = {
        'photos': dummy
    }
    return render(request, 'FlickrApp/index.html', context)
