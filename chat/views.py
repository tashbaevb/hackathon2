from rest_framework import generics
from .models import PromptResponse
from .serializers import PromptResponseSerializer


class PromptResponseAPIView(generics.ListCreateAPIView):
    queryset = PromptResponse.objects.all()
    serializer_class = PromptResponseSerializer


class DetailPromptResponse(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromptResponse.objects.all()
    serializer_class = PromptResponseSerializer
