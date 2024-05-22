from rest_framework import serializers
from .models import Publications


class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'


class PublicationsGetSerializer(serializers.ModelSerializer):
    publications = serializers.SerializerMethodField(method_name='get_publications', read_only=True)

    class Meta:
        model = Publications
        fields = ('id', 'publications')

    def get_publications(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'en':
                return obj.publications_en
            return obj.publications_uz
        except KeyError:
            return obj.publications_uz
