from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
import sys
sys.path.append("..")
from posts.models import Posts
from django.db.models import Q
from posts.forms import UploadForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
class Signup(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'

class homepageafterloged(ListView):
    model=Posts
    template_name="home.html"

class Cat(ListView):
    model=Posts
    template_name='Category.html'
    def get_queryset(self):
        query=self.request.GET.get('c')
        object_list=Posts.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
def Upload(request):
    submit=False
    form=UploadForm(request.POST,request.FILES)
    if request.method=='POST':
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/upload?submit=true')
    else:
        form=UploadForm
        if 'submit' in request.GET:
            submit=True
    return  render(request,'upload.html',{'form':form ,'submit':submit})
