from rest_framework import serializers

from .models import PromptResponse


class PromptResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptResponse
        fields = ("id", "prompt", "response")
