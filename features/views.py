from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    # blogs = Blog.objects.all()[:3]
    gallery = Gallery.objects.all()
    try:
        home = HomeContent.objects.all()[:1].get()
    except HomeContent.DoesNotExist:
        home = None
    context = {
        'products':products,
        'gallery':gallery,
        'home':home,
    }
    return render(request,'index.html',context)

def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products.html',context)


def product_details(request,id):
    product = Product.objects.get(id=id)
    products = Product.objects.exclude(id=id)
    context = {
        'products':products,
        'product':product,
    }
    return render(request, 'product_description.html',context)



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_obj = Contact.objects.create( name=name,email=email,contact=contact,subject=subject,message=message)
        contact_obj.save()
        return redirect('contact')
    else:
        return render(request,'contact.html')
    

def about_us(request):
    try:
        about = AboutPageContent.objects.all()[:1].get()
    except:
        about = None
    try:
        believe = WeBelieveIn.objects.all()[:1].get()
    except:
        believe = None

    context = {
        'about': about,
        'believe':believe,
    }
    return render(request,'about_us.html',context)
    