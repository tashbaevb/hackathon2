from django.urls import path

from .views import DetailPromptResponse, PromptResponseAPIView

urlpatterns = [
    path("prompts", PromptResponseAPIView.as_view(), name="prompt_list"),
    path("prompts/<int:pk>/", DetailPromptResponse.as_view(), name="prompt_detail"),
]
