from rest_framework import serializers
from .models import *

class QuickPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickPanel
        fields = '__all__'