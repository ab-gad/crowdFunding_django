from django.shortcuts import render
from .models import Test_simulation


data = Test_simulation.objects.all()
def home (request):
    # for project in
    return render(request , 'home.html' , {'name': data})

def error (request):
    return render(request , '404.html')

def search (request):
    if request.method == 'POST' and request.POST['search']:
        search = request.POST['search']
        projects = Test_simulation.objects.filter(title_simulation__contains = search )
        if projects :
            return render(request , 'search_page.html' , {'search' : projects , 'name': data })
        else:
            return render(request , 'search_page.html' , {'msg' : 'No Result' , 'name': data })
    else:
        return render(request , 'search_page.html' , {'msg' : 'No Result' , 'name': data })
  