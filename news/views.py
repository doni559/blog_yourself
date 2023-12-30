from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, EditArticlesForm
from django.views.generic import DetailView,  UpdateView, DeleteView
import datetime
from math import ceil



def news_detail_view(request, pk):
    article=Articles.objects.get(id=pk)
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "article":article
    }
    return render(request, 'news/detail_view.html',data)

def article_delete(request, pk):
    article=Articles.objects.get(id=pk)

    data={
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "article":article
    }
    return render(request, 'news/article_delete.html',data)
def article_delete_delete(request, pk):
    return redirect('/')

def article_delete_cancel(request, pk):
    return redirect('/')

def article_edit(request, pk):
    article=Articles.objects.get(id=pk)
    if request.method=="POST":
        form= EditArticlesForm(request.POST)
        
        if form.is_valid():
            title=form.cleaned_data.get("title")
            anounce=form.cleaned_data.get("anounce")
            full_text=form.cleaned_data.get("full_text")
            article.title=title
            article.anounce=anounce
            article.full_text=full_text

            article.save()
            return redirect('/')
        else:
            error="Форма была неверной"
    form = EditArticlesForm()
    data={
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "form": form
    }
    return render(request, 'news/add_article.html',data)


def news_home(request, page):
    all_news=Articles.objects.order_by("-date")
    news=all_news[((page-1)*8):8*page]

    max_page=ceil(len(all_news)/8)
    data={
        "news":news,
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "page": page,
        "max_page":max_page,
        "prev_page": page-1,
        "next_page": page+1
    }
    return render(request, 'news/news_home.html',data)

def add_article(request):
    error=""
    if request.method=='POST':
        form= ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error="Форма была неверной"
    form = ArticlesForm()
    data= {
        "user" : request.user,
        "auth": request.user.is_authenticated,
        "form": form,
        "error": error,
        "date": {
            "year": datetime.datetime.now().year,
            "month":datetime.datetime.now().month,
            "day":datetime.datetime.now().day,
        }
    }
    return render(request, 'news/add_article.html', data)
