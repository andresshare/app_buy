from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {'title': 'Hello index',
               'content':  'Welcome to Home',
               }
    if request.user.is_authenticated():
        context['premium_content'] = "Ohh Yeahhh"
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {'title': 'About',
               'content': 'Welcome to About'}
    return render(request, 'about_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {'title': 'Contact',
               'content': 'Welcome to Contact',
               'form': contact_form}

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    #if request.method == "POST":
    #print(request.POST)
    #print(request.POST.get('fullname'))
    #print(request.POST.get('email'))
    #print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")

    return  render(request, "auth/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", context)




