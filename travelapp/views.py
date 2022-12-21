from django.http import HttpResponse
from django.shortcuts import render
from . models import Destination

def index(request):
   dests= Destination.object.all()
   return render(request,'index.html',{'dests':dests})

def contact(request):
      return render(request, 'contact.html')
