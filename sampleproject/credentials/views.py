from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':

        uname=request.POST['username']
        psw = request.POST['password']
        user=auth.authenticate(username=uname,password=psw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        psw=request.POST['password']
        cpsw=request.POST['cpassword']
        if psw==cpsw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=psw,first_name=fname,last_name=lname,email=email)
                user.save();
#                # print("User Created")
        else:
            messages.info(request,"Password not Matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


