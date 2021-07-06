from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html',)
def password(request):

    thepassword = ''

    # The list of characters used
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get("length"))

    if (request.GET.get('Uppercase')):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if (request.GET.get('Special')):
            characters.extend(list("!?><{}()@#$%^&*~"))

    if (request.GET.get('Numbers')):
        characters.extend(list("123456789"))

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request,'generator/password.html', {'password':thepassword})