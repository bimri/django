from re import search
from typing_extensions import Required
from urllib import request
from django import forms
from numpy import require
from .models import Publisher

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceWidget(
        required=False, choices=(("title", "Title"), ("contributor", "Contributor"))
    )


class PubliserForm(forms.Form):
    class Meta:
        model = Publisher 
        fields = "__all__"
