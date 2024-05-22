from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicationsViewSet

router = DefaultRouter()
router.register(r'publications', PublicationsViewSet)

urlpatterns = router.urls

urlpatterns += [

]
