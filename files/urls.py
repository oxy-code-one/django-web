from django.urls import path
from .views import index,image
from .views import HomePageView
urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('img',image,name='image'),
    path('ip',index),
]