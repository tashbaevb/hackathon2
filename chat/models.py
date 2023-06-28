from django.db import models


class PromptResponse(models.Model):
    prompt = models.CharField(max_length=250)
    response = models.TextField()

    def __str__(self):
        return self.prompt
