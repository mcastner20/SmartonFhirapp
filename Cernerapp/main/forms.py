from django import forms
from .models import Information
class DateInput(forms.DateInput):
    input_type = 'date'
class Informations(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    class Meta:
        model = Information
        fields = ('first_name', 'last_name', 'date_of_birth')