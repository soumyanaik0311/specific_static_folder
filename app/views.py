from django.shortcuts import render

# Create your views here.

def specific_img(request):
    return render(request,'specific_img.html')
