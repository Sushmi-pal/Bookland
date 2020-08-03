from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.
def mainpage(request):
    return render(request,'begin/index.html')

def home(request):
    return render(request,'begin/base.html')

def aboutus(request):
    return render(request,'begin/about-us.html')

def service(request):
    return render(request,'begin/service.html')

def contact(request):
    if request.method=='POST':
        print(request.POST)
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)
        if len(name)<1 or len(email)<3 or len(phone)<5 or len(content)==0:
            messages.error(request,'Please fill the form correctly')
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your message has been successfully sent')


    return render(request,'begin/contact.html')