from django.contrib.auth import login as dj_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, EditProfile
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import AllUsersData

def edit(request, username):
    if request.user.username == username:
        if request.method == 'POST':
            form = EditProfile(request.POST)
            if form.is_valid():
                about = form.cleaned_data.get('about')
                status = form.cleaned_data.get('status')

                user_data=AllUsersData.objects.get(username=username)

                user_data.about=about
                user_data.status=status

                user_data.save()
                return redirect('/')
        else:
            form = EditProfile()
        data={
            "user" : request.user,
            "auth": request.user.is_authenticated,
            "form": form
        }
        return render(request, 'user/edit_profile.html', data)
    else:
        redirect('/')


def quit(request):
    logout(request)
    return redirect('/')

# Create your views here.
def login(request):
    error=''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('nickname')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "form": form
    }
    return render(request, 'user/login.html', data)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            AllUsersData.objects.create(username=username, about='', status='')
            return redirect('/')
    else:
        form = UserCreationForm()
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "form" : form
    }
    return render(request, 'user/register.html', data)

def your_profile(request, username):
    all_users_info=AllUsersData.objects.all()
    user_profile=all_users_info.get(username=username)
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "profile": user_profile
    }
    if(data["profile"].username == data["user"].username):
        print(data["user"])

    return render(request, 'user/your_profile.html', data)