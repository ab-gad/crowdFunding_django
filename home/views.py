from django.shortcuts import render
from .models import Test_simulation
from django.shortcuts import redirect

data = Test_simulation.objects.all()
last_5_projects = data.order_by('-id')[:5]

def home (request):
    return render(request , 'home.html' , {'name': data , 'last_5_projects':last_5_projects})

def error (request):
    return render(request , '404.html')

def search (request):
    try:
        if request.method == 'POST' and request.POST['search']:
            search = request.POST['search']
            projects = Test_simulation.objects.filter(title_simulation__contains = search )
            if projects :
                return render(request , 'search_page.html' , {'search' : projects , 'name': data })
            else:
                return render(request , 'search_page.html' , {'msg' : 'No Result' , 'name': data })
        else:
            return render(request , 'search_page.html' , {'msg' : 'No Result' , 'name': data })
    except:
        return redirect(error)
