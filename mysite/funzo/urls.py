from django.conf.urls import url

from . import views

# ^ beginning of string
# $ end of string

#url(what to look for, what function to grab, name of this url)

urlpatterns = [
    url(r'^index$', views.index, name = 'index'), #this grabs the index from views.py
]
