from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):

    return render (request, "index.html")



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("account_app:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email  already registered")
                return redirect("account_app:register")
            else:
                user = User.objects.create_user(username=username, email=email,
                                        password=password1)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('account_app:register')
        return redirect("account_app:index")
    else:
         return render(request,"registration.html")



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect("account_app:index")
        else:
            messages.info(request,"invalid details")
            return redirect("account_app:login")
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")

         
