from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SphereViewSet, PapersViewSet, ReviewersViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'spheres', SphereViewSet)
router.register(r'papers', PapersViewSet)
router.register(r'reviewers', ReviewersViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
