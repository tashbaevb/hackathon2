from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView, ProfileDetailAPIView, \
    ProfileUpdateAPIView
from django.urls import path

urlpatterns = [
    path('signup/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserAPI.as_view(), name='user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('profile/', ProfileDetailAPIView.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),
]

