# from unicodedata import category 
from django.shortcuts import render
from campaign.models import Campaign, Category, Rating
from django.shortcuts import redirect

data = Campaign.objects.all()
last_5_projects = data.order_by('-id')[:5]
highest_5_projects = Rating.objects.all().order_by('-value')[:5]

categories = Category.objects.all()


def home(request):
    length = len(data)
    return render(request, 'home.html', {'category': categories,
                                         'last_5_projects': last_5_projects,
                                         'highest_5_projects': highest_5_projects,
                                         'length': length,
                                         })


def error(request):
    return render(request, '404.html')


def search(request):
    try:
        if request.method == 'POST' and request.POST['search']:
            search = request.POST['search']

            projects = Campaign.objects.filter(title__contains=search)
            if projects:
                return render(request, 'search_page.html', {'search': projects,
                                                            'name': data,
                                                            'category': categories
                                                            })
            else:
                return render(request, 'search_page.html', {'msg': 'No Result', 'name': data, "category": categories})
        else:
            return render(request, 'search_page.html', {'msg': 'No Result', 'name': data, "category": categories})
    except:
        return redirect(error)


def category(request, categoty_id):
    try:
        if request.method == "GET":
            campaigns = Campaign.objects.filter(category=categoty_id)
            camplen = len(campaigns)
        return render(request, 'category.html', {'campaigns': campaigns,
                                                 'category': categories,
                                                 'camplen': camplen,
                                                 })

    except:
        return redirect(error)


def highest_projects(request, project_id):
    try:
        if request.method == "GET":
            highest_project = Campaign.objects.get(id=project_id)
        return render(request, 'highest_projects.html', {'highest_project': highest_project,
                                                         'category': categories
                                                         })

    except:
        return redirect(error)


def all_project(request):
    return render(request, 'all_project.html', {'all': data})
