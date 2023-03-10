from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Customers
from __future__ import unicode_literals
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'


def index(request):
    data = Customers.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def edit(request):
    return render(request, "edit.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        county = request.POST.get('county')
        destination = request.POST.get('destination')
        vehicle = request.POST.get('vehicle')
        amount = request.POST.get('amount')
        query = Customers(name=name, email=email, age=age, gender=gender, county=county, destination=destination,
                          amount=amount, vehicle=vehicle)
        query.save()
        return redirect("/")

        return render(request, "index.html")


def deleteData(request, id):
    d = Customers.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request="index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        county = request.POST.get('county')
        destination = request.POST.get('destination')
        vehicle = request.POST.get('vehicle')
        amount = request.POST.get('amount')

        update_Info = Customers.objects.get(id=id)
        update_Info.name = name
        update_Info.email = email
        update_Info.age = age
        update_Info.gender = gender
        update_Info.county = county
        update_Info.destination = destination
        update_Info.vehicle = vehicle
        update_Info.amount = amount

        update_Info.save()
        return redirect("/")
    d = Customers.objects.get(id=id)
    context = {"d": d}

    return render(request, "edit.html", context)

 def pay(request,id):
        if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'COCO'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request,'index.html')