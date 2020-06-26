from rest_framework import serializers
from .models import *


class TokenSz(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
