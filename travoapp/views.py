from django.shortcuts import render

from .models import travo


# Create your views here.
def demo(request):
    obj=travo.objects.all()
    return render(request,"index.html",{'result':obj})

