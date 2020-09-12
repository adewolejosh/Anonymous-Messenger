from django import forms
from .models import Text


class AmaForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ["note"]
