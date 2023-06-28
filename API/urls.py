from django.urls import path
from .views import InstituteAPI, InstituteEventAPI, ReviewAPI
from .views import ListInstituteAPI, ListInstituteEventAPI, ListReviewAPI, FilteredListInstituteAPI

urlpatterns = [
    path('api/v1/institutes', ListInstituteAPI.as_view(), name="institutesAPI"),
    path('api/v1/institutes/filter', FilteredListInstituteAPI.as_view(), name="institutesAPI"),
    path('api/v1/events', ListInstituteEventAPI.as_view(), name="eventsAPI"),
    path('api/v1/reviews', ListReviewAPI.as_view(), name="reviewsAPI"),
    path('api/v1/institutes/<int:pk>/', InstituteAPI.as_view(), name="institutesAPI"),
    path('api/v1/events/<int:pk>/', InstituteEventAPI.as_view(), name="eventsAPI"),
    path('api/v1/reviews/<int:pk>/', ReviewAPI.as_view(), name="reviewsAPI"),
]
