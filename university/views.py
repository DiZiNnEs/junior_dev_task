from django.shortcuts import render

from .models import University
from .forms import UniversityForm


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
