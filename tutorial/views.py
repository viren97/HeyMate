from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import tutorial,TutorialCategory, TutorialSeries
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .form import NewUserForm
from .models import tutorial
from django.db import models


# Create your views here.
def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] =part_one.tutorial_slug

        return render(request, "tutorial/categories.html",{"part_ones":series_urls} )

    tutorials = [t.tutorial_slug for t in tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = tutorial.objects.get(tutorial_slug = single_slug)
        tutorial_from_series = tutorial.objects.filter(tutorial_series__tutorial_series= this_tutorial.tutorial_series).order_by("tutorial_published")
        this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)
        return render(request,
                      "tutorial/tutorial.html",
                      {'tut':this_tutorial,
                       'sidebar':tutorial_from_series,
                       'this_tut_idx':this_tutorial_idx})
        return HttpResponse(f"{single_slug} is a tutorial")



    #return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

def homepage(request):
    return render(request, "tutorial/category.html", {"categories":TutorialCategory.objects.all()})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"welcome : {username}")
            login(request, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form= NewUserForm()
    return render(request, "tutorial/register.html", {'form':form})


def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"you are logged in as : {username}")
                return redirect("/")
            else:
                messages.error(request, f"username or password is incorrect")
        else:
           messages.error(request, f"username or password is incorrect")

    form = AuthenticationForm()
    return render(request, "tutorial/login.html", {'form':form})


def logout_request(request):
    logout(request)
    messages.info(request, f"logout out successsfully")
    return redirect("/")
