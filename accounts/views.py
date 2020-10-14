from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'account.html')
