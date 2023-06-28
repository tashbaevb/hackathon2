from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("rest_framework.urls")),
    path("", include("accounts.urls")),
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("api/chat/", include("chat.urls")),
    path("api/API/", include("API.urls")),
]
