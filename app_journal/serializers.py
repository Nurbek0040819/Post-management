from rest_framework import serializers
from .models import Contact, FAQ, Requirements


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'email', 'message']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class FAQGetSerializer(serializers.ModelSerializer):
    faq_question = serializers.SerializerMethodField(method_name='get_faq_question', read_only=True)

    class Meta:
        model = FAQ
        fields = ('id', 'faq_question')

    def get_faq_question(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'eng':
                return obj.faq_question_eng
            return obj.faq_question_uz
        except KeyError:
            return obj.faq_question_uz


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class RequirementsGetSerializer(serializers.ModelSerializer):
    requirements = serializers.SerializerMethodField(method_name='get_requirements', read_only=True)

    class Meta:
        model = Requirements
        fields = ('id', 'requirements')

    def get_requirements(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'eng':
                return obj.requirements_eng
            return obj.requirements_uz
        except KeyError:
            return obj.requirements_uz

