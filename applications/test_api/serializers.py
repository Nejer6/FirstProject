from rest_framework import serializers

from .models import *


class PetRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name']


class PersonSerializer(serializers.ModelSerializer):
    pets = PetRelSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'
