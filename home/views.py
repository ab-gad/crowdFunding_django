from unicodedata import category
from django.shortcuts import render 
from campaign.models import Campaign , Category , Rating
from django.shortcuts import redirect

data = Campaign.objects.all()
last_5_projects = data.order_by('-id')[:5]
highest_5_projects = Rating.objects.all().order_by('-value')[:5]
categories = Category.objects.all()

def home (request):
    return render(request , 'home.html' , {'category' : categories , 'last_5_projects':last_5_projects , 'highest_5_projects':highest_5_projects})

def error (request):
    return render(request , '404.html')

def search (request):
    try:
        if request.method == 'POST' and request.POST['search']:
            search = request.POST['search']

            projects = Campaign.objects.filter(title__contains = search )
            if projects :
                return render(request , 'search_page.html' , {'search' : projects , 'category' : categories , 'name': data })
            else:
                return render(request , 'search_page.html' , {'msg' : 'No Result' , 'category' : categories , 'name': data })
        else:
            return render(request , 'search_page.html' , {'msg' : 'No Result' ,'category' : categories , 'name': data })
    except:
        return redirect(error)
        

def category(request, categoty_id):
    try:
        if request.method == "GET":
            campaigns = Campaign.objects.filter(category=categoty_id)
        return render(request, 'category.html', {"campaigns": campaigns, "category": categories})
    
    except:
        return redirect(error)

