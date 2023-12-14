from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from tkinter import *
root=Tk()


# Create your views here.




def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        dob = request.POST['dob']
        age = request.POST['age']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        materials_provided = request.POST['materials_provided']
        debit_card = request.POST.get['debit_card']
        credit_card = request.POST.get['credit_card']
        cheque_book = request.POST.get['cheque_book']
        dropdownitem = request.POST.get['dropdownitem']




        return redirect('form')


    return render(request,"form.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

                user.save()
                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')