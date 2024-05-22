from rest_framework import viewsets
from .models import Sphere, Papers, Reviewers, Feedback
from .serializers import SphereSerializer, PapersSerializer, ReviewersSerializer, FeedbackSerializer
from .permissions import IsAuthenticated
from .filters import PapersFilter
from django_filters.rest_framework import DjangoFilterBackend


class SphereViewSet(viewsets.ModelViewSet):
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializer
    permission_classes = [IsAuthenticated]


class PapersViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = PapersSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PapersFilter


class ReviewersViewSet(viewsets.ModelViewSet):
    queryset = Reviewers.objects.all()
    serializer_class = ReviewersSerializer
    permission_classes = [IsAuthenticated]


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]