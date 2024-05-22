from rest_framework import serializers
from .models import Sphere, Papers, Reviewers, Feedback
from app_publications.serializers import PublicationsSerializer


class SphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sphere
        fields = '__all__'


class PapersSerializer(serializers.ModelSerializer):
    publication_id = PublicationsSerializer()

    class Meta:
        model = Papers
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class PaperGetSerializer(serializers.ModelSerializer):
    paper = serializers.SerializerMethodField(method_name='get_paper', read_only=True)

    class Meta:
        model = Papers
        fields = ('id', 'paper')

    def get_paper(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.paper_en
            return obj.paper_uz
        except KeyError:
            return obj.paper_uz


class ReviewersSerializer(serializers.ModelSerializer):
    sphere_id = SphereSerializer(many=True)

    class Meta:
        model = Reviewers
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
