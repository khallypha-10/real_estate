from django.shortcuts import render, redirect
from . models import House, Agents, Profile
from .forms import HouseForm, SignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def navbar(request):
    agents = Agents.objects.all()
    context = {"agents": agents}

    return render(request, "estate/agents.html", context)



def home(request):
    houses= House.objects.all()
    

    context={"houses": houses}
    return render(request, "estate/home.html", context)


def profile(request, user):
    users = Agents.objects.all()
    user = Profile.objects.get(user= request.user)
    

    context ={"user": user, "users": users }
    return render(request, "estate/profile.html", context)

def edit_profile(request, id):
    form = Agents.objects.get(id=id)
    frm = ProfileForm(instance=form)
    if request.method == 'POST':
        frm = ProfileForm(request.POST, instance=form)
        if frm.is_valid():
            frm.save()
            return redirect("home")
    context = {"frm": frm}
    return render(request, "estate/edit_profile.html", context)


def register(request):
    form = SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "estate/register.html", context)




def search(request):
    if request.method == "POST":
        searched = request.POST['q']
        names = House.objects.filter(
            name__icontains= searched 
            )

    context = {"searched": searched, "names": names}
    return render(request, "estate/searched_for.html", context)


    

def about_us(request):
    return render(request, "estate/about.html")



def contact(request):
    return render(request, "estate/contact.html")




    

@login_required(login_url='login')
def property_detail(request, id):
    detail = House.objects.get(id=id)
    context = {"detail": detail}
    return render(request, "estate/details.html", context)

def pricing(request):
    house = House.objects.all()
    
    context = {"house": house}
    return render(request, "estate/pricing.html", context)

