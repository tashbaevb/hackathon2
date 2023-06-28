from django.contrib import admin

from .models import PromptResponse


class PromptResponseAdmin(admin.ModelAdmin):
    list_display = (
        "prompt",
        "response",
    )


admin.site.register(PromptResponse, PromptResponseAdmin)
