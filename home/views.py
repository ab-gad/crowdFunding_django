from django.shortcuts import render

def home (req):
    return render(req , 'home.html')

def error (req):
    return render(req , '404.html')

