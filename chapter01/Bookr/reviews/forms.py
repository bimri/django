from re import search
from typing_extensions import Required
from urllib import request
from django import forms
from numpy import require


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceWidget(
        required=False, choices=(("title", "Title"), ("contributor", "Contributor"))
    )
