from django import forms
from .models import MyModel,NameModel

class ModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields='__all__'

class NameForm(forms.ModelForm):
    class Meta:
        model = NameModel
        fields='__all__'
