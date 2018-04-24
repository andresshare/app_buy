from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {'title': 'Hello index',
               'content':  'Welcome to Home'}

    return render(request, 'home_page.html', context)


def about_page(request):
    context = {'title': 'About',
               'content': 'Welcome to About'}
    return render(request, 'about_page.html', context)


def contact_page(request):
    context = {'title': 'Contact',
               'content': 'Welcome to Contact'}
    if request.method == "POST":
        print(request.POST)
    return render(request, 'contact/view.html', context)