from flendzz.models import student
from rest_framework import serializers 
from flendzz.models import student

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'