from django.urls import include, path
from accounts.views import Signup,homepageafterloged,Cat,Upload

urlpatterns = [
    path('user/',homepageafterloged.as_view(),name='logged')
    ,path('signup/',Signup.as_view(),name='signup')
    ,path('cat/',Cat.as_view(),name='catafterlog')
    ,path('upload/',Upload,name='upload')
]