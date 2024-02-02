
from django.contrib import admin
from django.urls import path
from posts.views import home,show
urlpatterns = [
   path("",home,name = "home"),
   path("show/",show,name = "show")
]
