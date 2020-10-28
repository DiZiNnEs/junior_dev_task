from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth.decorators import login_required

from .models import University
from .forms import UniversityForm


def register_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('form is not valid')
    else:
        print('request is not POST')

    context = {'form': form}
    return render(request, 'university/authentication/register.html', context)


def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('form is not valid')
    else:
        print('request is not POST')

    context = {'form': form}
    return render(request, 'university/authentication/login.html', context)


@login_required(login_url='sign-in')
def main(request):
    form = UniversityForm()

    if request.method == 'POST':
        print(request.POST)
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()

    database = University.objects.all()
    context = {'university': database,
               'form': form}
    return render(request, 'university/index.html', context)


def university_page_delete(request, pk):
    database = University.objects.get(id=pk)
    if request.method == "POST":
        database.delete()
        return redirect('/')

    context = {'university': database}
    return render(request, 'university/university_page.html', context)
