from django.shortcuts import render
from  django.http import HttpResponse
from .import models


def home(request):
    post_list = models.Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
