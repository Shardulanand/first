from django import forms
from app2.models import *

class Food_Form(forms.ModelForm):
    class Meta:
        model=Food
        fields=('name','price','description','image')