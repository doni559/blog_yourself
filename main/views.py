from django.shortcuts import render



# Create your views here.
def index(request):
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated
    }
    return render(request, 'main/home.html', data)
def about(request):
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated
    }
    return render(request, 'main/about.html', data)
