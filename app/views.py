from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages

def test(request):
    return HttpRespose("led on")
    


def led(request):

    print(visitor_ip_address(request))
    if request.method == "POST":
        pass

    if request.method == "GET":
        return render(request , "led.html")
    

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def app(request):

    return render(request , "index.html")

def login(request):

    dict_1 = {}
    if request.method == "POST":
        username = request.POST["user"]
        lastname = request.POST["last_name"]
        firstname = request.POST["first_name"]
        email = request.POST["Email"]
        password = request.POST["password1"]
        password2 = request.POST["password2"]
        dict_1 = [ password , password2]
        print(firstname ,lastname ,username)

        if username == "" or firstname == "" or email == "" :
            messages.info(request, "Enter the credentials ")
            return redirect("/login")

        if password != password2:

            messages.info(request,'password not matching..')    
            return redirect("/led")

        
        
       
        return render(request , "login.html"  )
    if request.method == "GET":
        return render(request , "Slogin.html")    