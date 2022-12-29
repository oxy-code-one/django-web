"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from log.views import home_view
from log.views import insert_view
from log.views import get_data_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = "home"),
    path('insert/', insert_view, name = "insert"),
    path('get/', get_data_view, name = "get_data"),
    path('file/', include('files.urls')),
]
