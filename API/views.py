from django.db.models import Q
from rest_framework import generics
from .models import Institute, InstituteEvent, Review
from .serializers import InstituteSerializer, InstituteEventSerializer, ReviewSerializer


class FilteredListInstituteAPI(generics.ListCreateAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

    def filter_by_city_or_region(self, request):
        city = request.GET.get('city_or_reg')
        region = request.GET.get('region')
        possessiveness = request.GET.get('possessiveness')
        queryset = self.queryset

        if city:
            queryset = queryset.filter(city_or_reg=city)
        elif region:
            queryset = queryset.filter(region=region)
        elif possessiveness:
            queryset = queryset.filter(possessiveness=possessiveness)

        return queryset

    def filter_by_search_query(self, queryset, search_query):
        if search_query:
            queryset = queryset.filter(
                Q(city_or_reg__icontains=search_query) |
                Q(region__icontains=search_query) |
                Q(possessiveness__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset

    def get_queryset(self):
        queryset = self.filter_by_city_or_region(self.request)
        search_query = self.request.GET.get('search')
        queryset = self.filter_by_search_query(queryset, search_query)
        return queryset


class ListInstituteAPI(generics.ListCreateAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class InstituteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class ListInstituteEventAPI(generics.ListCreateAPIView):
    queryset = InstituteEvent.objects.all()
    serializer_class = InstituteEventSerializer


class InstituteEventAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstituteEvent.objects.all()
    serializer_class = InstituteEventSerializer


class ListReviewAPI(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
