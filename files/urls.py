from django.urls import path
from .views import index,image
urlpatterns = [
    path('',index,name='index'),
    path('img',image,name='image'),
]