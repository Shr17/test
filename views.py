from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Article, Blogger
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic, View
# from .forms import UserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from core.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import datetime


# from .forms import SnippetForm, ContactForm, LoginForm


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'testapp/login.html')
    else:
        article_results = Article.objects.all()
        query = request.GET.get("q")
        if query:

            article_results = article_results.filter(
                Q(song_headline__icontains=query)
            ).distinct()
            return render(request, 'testapp/index.html', {

                'articles': article_results,
            })
        else:
            return render(request, 'testapp/index.html', {'articles': article_results})




# def index(request):
#     if not request.user.is_authenticated:
#         return render(request, 'testapp/login.html')
#     else:
#         bloggers = Blogger.objects.filter(user=Blogger.id)
#         article_results = Article.objects.all()
#         query = request.GET.get("q")
#         if query:
#             bloggers = bloggers.filter(
#                 Q(blogger_name__icontains=query)).distinct()
#             article_results = article_results.filter(
#                 Q(headline__icontains=query)
#             ).distinct()
#             return render(request, 'testapp/index.html', {
#                 'bloggers': bloggers,
#                 'articles': article_results,
#             })
#         else:
#             return render(request, 'testapp/index.html', {'bloggers': bloggers})


def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("This article does not exist")
    return render(request, 'testapp/detail.html', {'article': article})
