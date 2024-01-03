from rest_framework import serializers
from .models import ContactModels

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModels
        fields = '__all__'
