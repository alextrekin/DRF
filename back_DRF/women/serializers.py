from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
import io
from  rest_framework.parsers import JSONParser


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

