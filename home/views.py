from urllib import request
from django.shortcuts import render 
from taggit.models import TaggedItem
from campaign.models import Campaign, Category, Rating 
from django.shortcuts import redirect

data = Campaign.objects.all()
last_5_projects = data.order_by('-id')[:5]
highest_5_projects = Rating.objects.all().order_by('-value')[:5]
categories = Category.objects.all()

def home(request):
    length = len(data)
    features_projects = Campaign.objects.filter(is_featured='t')  
    return render(request, 'home.html', {'category': categories,
                                         'last_5_projects': last_5_projects,
                                         'highest_5_projects': highest_5_projects,
                                         'length': length,
                                         'features_projects':features_projects,
                                        })

def error(request):
    return render(request, '404.html')

def search(request):
    try:
        if request.method == 'POST' and request.POST['search']:
            search = request.POST['search']
            tags = Campaign.tags.filter(name__contains = search)
            projects = Campaign.objects.filter(title__contains=search)
            if projects or tags:
                return render(request, 'search_page.html', { 'search': projects,
                                                             'category': categories,
                                                             'tags':tags,
                                                            })
            else:
                return render(request, 'search_page.html', { 'msg': 'No Result',
                                                             'category': categories,
                                                            })
        else:
            return render(request, 'search_page.html', { 'msg': 'No Result' ,
                                                         'category': categories,
                                                        })
    except:
        # return redirect(error)
        pass


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
