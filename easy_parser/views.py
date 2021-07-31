from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    context = {'city': city, 'language': language, 'form': form}
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

        qs = Vacancy.objects.filter(**_filter).select_related('city', 'language')

    return render(request, 'easy_parser/home.html', {'object_list': qs, 'form': form})
