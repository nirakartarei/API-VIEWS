from app.models import *
from rest_framework import serializers


class products(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
