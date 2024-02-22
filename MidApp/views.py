from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')
def AboutUs(request):
    return render(request,'about_us.html')
def Contact(request):
    return render(request,'contact.html')
def Gallery(request):
    return render(request,'Gallery.html')