from rest_framework.response import Response
from rest_framework import status, generics
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .models import Contact, FAQ, Requirements
from .permissions import IsSuperUserORReadOnly
from .serializers import (
    ContactSerializer,
    FAQSerializer, FAQGetSerializer,
    RequirementsSerializer, RequirementsGetSerializer,
)


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        if self.request.user.is_authenticated:
            self.send_email_to_admins(contact)
        return Response({"message": "Contact message sent successfully"}, status=status.HTTP_201_CREATED)

    def send_email_to_admins(self, contact):
        User = get_user_model()
        admins = User.objects.filter(is_staff=True)

        admin_emails = [admin.email for admin in admins]

        send_mail(
            subject=f"New contact message from {contact.user.username}",
            message=contact.message,
            from_email=contact.email,
            recipient_list=admin_emails,
            fail_silently=False,
        )


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    permission_classes = [IsSuperUserORReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FAQGetSerializer
        return FAQSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class RequirementViewSet(ModelViewSet):
    queryset = Requirements.objects.all()
    permission_classes = [IsSuperUserORReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RequirementsGetSerializer
        return RequirementsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save
