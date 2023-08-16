from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    gallery = Gallery.objects.all()
    try:
        home = HomeContent.objects.all()[:1].get()
    except HomeContent.DoesNotExist:
        home = None
    context = {
        'blogs':blogs,
        'products':products,
        'gallery':gallery,
        'home':home,
    }
    return render(request,'index.html',context)
