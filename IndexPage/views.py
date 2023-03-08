from django.shortcuts import render, redirect
from IndexPage import models


def index(request):

    return render(request, 'index.html')


def get_data(request):
    obj = models.TStatWorkRelation.objects.filter(id=1).first()
    print(obj.id)
    return render(request, 'index.html', {'row': obj})
