from unicodedata import category
from django.shortcuts import render , get_object_or_404
from campaign.models import Campaign , Category
from django.shortcuts import redirect

data = Campaign.objects.all()
last_5_projects = data.order_by('-id')[:5]
categories = Category.objects.all()

def home (request):
    return render(request , 'home.html' , {'category' : categories , 'last_5_projects':last_5_projects})

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

    if request.method == "GET":
        categ = get_object_or_404(Category, id=categoty_id)
        campaigns = Campaign.objects.filter(category=categoty_id)

    return render(request, 'category.html', {"campaigns": campaigns,"categ": categ, "category": categories})
# /home/category/2