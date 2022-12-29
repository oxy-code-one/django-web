from io import BytesIO
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from PIL import Image
import os
# Create your views here.
pwd = os.path.dirname(__file__)

def index(request, *args, **kwargs):
    return render(request,'static/index.html')

def image(request, *args, **kwargs):
    img = Image.open(pwd+'/image.jpeg')
    fomatted_img = BytesIO()
    img.save(fomatted_img, format="jpeg")
    response = HttpResponse(fomatted_img.getvalue(),content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename="lol.jpeg"'
    return response

class HomePageView(TemplateView):
    template_name = "home.html"