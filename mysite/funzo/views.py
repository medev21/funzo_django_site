from django.http import HttpResponse
from django.shortcuts import render

import random
# Create your views here.

def index(request):
    pic_url = random.choice((
        'https://tstoaddicts.files.wordpress.com/2013/11/funzo2.jpg',
        'https://tstoaddicts.files.wordpress.com/2013/11/funzos-3.jpg',
        'https://i.imgur.com/ECG486D.png',
        'http://www.kvrx.org/sites/default/files/styles/user-image/public/staffphotos/funzo0sf.png.jpeg?itok=A7xl6f5V'
    ))

    context = {
        'pic_url' : pic_url,
        'var1' : True,
    }

    return render(request, 'funzo/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index")
