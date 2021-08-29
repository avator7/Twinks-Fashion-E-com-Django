from django.shortcuts import render,redirect, HttpResponse
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def about(request):
    return render(request, 'Home/about.html')

def conatct(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        print(message)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "Home/contact.html")


def handleSignUp(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        number=request.POST['number']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
            
        #error handling

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')

            #creating user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.number=number
        myuser.pass2=pass2
        myuser.save()
        messages.success(request, "Your regestred now ")
        return redirect('home')
             
    

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        password=request.POST['password']
        user=authenticate(username= loginusername, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
        


def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
