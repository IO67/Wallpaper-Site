from django.urls import path,include
from posts.views import  Cat, Search, homepageposts

urlpatterns = [
    path('',homepageposts.as_view(),name='home')
    ,path('search/',Search.as_view(),name='search')
    ,path('cat/',Cat.as_view(),name='cat')
]