from multiprocessing import context
from turtle import home
from django.shortcuts import render,redirect
from app2.forms import *
from .models import *


def Homepage(request):
    return render(request,'app2/home.html')

def addFood(request):
    if request.method =="POST":
        form= Food_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect("app2:homepageurl")

    form=Food_Form()
    context={
        'form':form,
    }
    return render(request,'app2/add.html',context)

def foodlist(request):
    foodInst = Food.objects.all()
    context={
        'foodInst':foodInst,
    }
    return render(request,'app2/list.html',context)