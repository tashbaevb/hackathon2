from rest_framework import generics

from .models import PromptResponse
from .serializers import PromptResponseSerializer

# ACCURACY = 0.75


class PromptResponseAPIView(generics.ListCreateAPIView):
    queryset = PromptResponse.objects.all()
    serializer_class = PromptResponseSerializer


class DetailPromptResponse(generics.RetrieveUpdateDestroyAPIView):
    queryset = PromptResponse.objects.all()
    serializer_class = PromptResponseSerializer


# def check_word(word, prompt):
#     count = 0
#     w_list = list(word)
#     p_list = list(prompt)
#
#     min_len = min(len(w_list), len(p_list))
#     #queryset = PromptResponse.objects.get(pk=1).values()
#
#     for i in range(min_len):
#         if w_list[i] == p_list[i]:
#             count += 1
#
#     percent = count / min_len
#
#     if percent > ACCURACY:
#         return prompt
#     else:
#         return "Извините, но я ничего не нашел по вашему запросу"