from django.shortcuts import render
from .models import University


def main(request):
    database = University.objects.all()
    context = {'university': database}
    return render(request, 'university/index.html', context)
