from django.urls import path
from rest_framework import routers

from .views import ContactCreateView, FAQViewSet, RequirementViewSet

router = routers.DefaultRouter()
router.register(r'faq', FAQViewSet, basename='faq')
router.register(r'requirements', RequirementViewSet, basename='requirements')

urlpatterns = router.urls

urlpatterns += [
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
]
