from django import forms
from .models import ShortLink


class ShortForm(forms.ModelForm):
    longer_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Please, paste your link here"}))

    class Meta:
        model = ShortLink

        fields = ('longer_url', )
