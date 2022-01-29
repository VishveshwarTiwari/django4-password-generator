from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    #return render(request, 'generator/home.html',{'password':'abcdefgh@1234'})
    return render(request, 'generator/home.html')

    # Logic will be written in view and the visual part in the TEMPLATES
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        thepassword += random.choice(characters)
        #print(x)
    return render(request,'generator/password.html',{'password':thepassword})




def about(request):
    return render(request,'generator/about.html')
def vishu(request):
    return HttpResponse("<h1>Janmdivas ki hardik Shubhkamnayein</h1>")
def bhagwan(request):
    return HttpResponse("Bhagwan Shriram aur Hanumanji ki kripa tumpe bani rahe")
def future(request):
    return HttpResponse("Aasha hai aanewale samay me tumhe apne kshetra me safalta mile")
