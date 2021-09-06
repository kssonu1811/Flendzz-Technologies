from django.db.models import fields
from django.forms import ModelForm
from .models import student

class Orderform(ModelForm):
    class Meta:
        model = student
        fields = '__all__'