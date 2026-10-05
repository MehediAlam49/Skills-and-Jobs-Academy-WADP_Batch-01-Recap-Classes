from rest_framework import serializers
from api_app.models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model= studentModel
        fields = '__all__'