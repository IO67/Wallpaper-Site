from django.views.generic import ListView

from .forms import UploadForm
from .models import Posts
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Posts

# Create your views here.
class homepageposts(ListView):
    model=Posts
    template_name="index.html"

class Search(ListView):
    model=Posts
    template_name='search_result.html'
    def get_queryset(self):
        query=self.request.GET.get('q')
        object_list=Posts.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
class Cat(ListView):
    model=Posts
    template_name='Category.html'
    def get_queryset(self):
        query=self.request.GET.get('c')
        object_list=Posts.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
