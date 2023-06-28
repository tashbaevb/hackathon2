from rest_framework import serializers
from .models import Institute, InstituteEvent, Review


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'


class InstituteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteEvent
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
