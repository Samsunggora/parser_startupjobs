from django import forms
from easy_parser.models import City, Prof_language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    language = forms.ModelChoiceField(queryset=Prof_language.objects.all(), to_field_name='slug', required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
