from rest_framework import viewsets
from .models import Publications
from .serializers import PublicationsSerializer
from .permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from app_paper.models import Sphere, Papers
from app_paper.serializers import SphereSerializer, PapersSerializer


class PublicationsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PublicationsViewSet(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PublicationsPagination
