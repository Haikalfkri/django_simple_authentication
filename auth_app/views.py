from django.shortcuts import render, redirect
from auth_app.forms import UserProfile, UserForm
from auth_app.models import UserInfo

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    forms = UserInfo.objects.all()
    return render(request, 'index.html', {'all_data':forms})

@login_required
def create(request):
    if request.method == "POST":
        user_profile = UserProfile(request.POST, request.FILES)
        
        if user_profile.is_valid():
            user_profile.save()            
            return redirect('index')
        else:
            print(user_profile.errors)

    else:
        user_profile = UserProfile()
    return render(request, 'create.html', {'form':user_profile})

@login_required
def update(request, id):
    data = UserInfo.objects.get(id=id)
    forms = UserProfile(initial={'nim':data.nim, 'kelas':data.kelas, 'jurusan':data.jurusan, 'foto':data.foto})
    
    if request.method == "POST":
        forms = UserProfile(request.POST, request.FILES, instance=data)
        if forms.is_valid():
            try:
                forms.save()
                return redirect('index')
            except:
                pass
        else:
            print(forms.errors)
    else:
        forms = UserProfile(instance=data)
        
    return render(request, 'update.html', {'data':forms, 'image':data})

@login_required
def delete(request, id):
    obj = UserInfo.objects.get(id=id)
    try:
        obj.delete()
        return redirect('index')
    except:
        pass
    
    
def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            return redirect('auth_app:login')
        
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()     
    
    return render(request, 'register.html', {'form':user_form, 'registered':registered})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("user not active")
        else:
            return HttpResponse("You account want to be hacked")
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('auth_app:login'))