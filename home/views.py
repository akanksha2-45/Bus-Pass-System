from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import Buypass
from home.models import Buyticket
from django.contrib import messages


# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is my aboutpage(/about)")

    return render(request, 'about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern = request.POST['concern']
        print(name, email, phone, concern)

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(concern)<2:
            messages.error(request, "Please fill the form correctly")
        else:
            ins = Contact(name=name, email=email, phone=phone, concern=concern)
            ins.save()
            messages.error(request, "Successfully Submitted")

        print('the data has been written to the db')
    return render(request, 'contact.html')


def buyticket(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender1 = request.POST['gender']
        stop01 = request.POST['stop1']
        stop02 = request.POST['stop2']
        print(name, email, phone, gender1, stop01, stop02)

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(gender1)<1 or len(stop01)<3 or len(stop02)<2:
            messages.error(request, "Please fill the form correctly.")
        else:
            ins = Contact(name=name, email=email, phone=phone, gender=gender1, stop1=stop01, stop2=stop02)
            ins.save()
            messages.error(request, "Successfully Submitted")

        print('the data has been written to the db')
    return render(request, 'buyticket.html')


def buypass(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender2 = request.POST['gender']
        durationtype = request.POST['duration']
        print(name, email, phone, gender2, durationtype)

        if len(name)<2 or  len(email)<5 or len(phone)<10 or len(gender2)<1 or len(durationtype)<2:
            messages.error(request, "Please fill the form correctly.")
        else:
            ins = Contact(name=name, email=email, phone=phone, gender=gender2, duration=durationtype)
            ins.save()
            messages.error(request, "Successfully Submitted")

        print('the data has been written to the db')
    return render(request, 'buypass.html')

def renew(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender2 = request.POST['gender']
        durationtype = request.POST['duration']
        print(name, email, phone, gender2, durationtype)

        if len(name)<2 or  len(email)<5 or len(phone)<10 or len(gender2)<1 or len(durationtype)<2:
            messages.error(request, "Please fill the form correctly.")
        else:
            ins = Contact(name=name, email=email, phone=phone, gender=gender2, duration=durationtype)
            ins.save()
            messages.error(request, "Successfully Submitted")

        print('the data has been written to the db')
    return render(request, 'renew.html')