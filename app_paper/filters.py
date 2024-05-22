from django_filters import rest_framework as filters
from .models import Sphere, Papers


class SphereFilter(filters.FilterSet):
    sphere_name = filters.CharFilter(field_name='sphere_name', lookup_expr='icontains')

    class Meta:
        model = Sphere
        fields = ['sphere_name']


class PapersFilter(filters.FilterSet):
    paper_title_uz = filters.CharFilter(field_name='paper_title_uz', lookup_expr='icontains')
    paper_title_en = filters.CharFilter(field_name='paper_title_en', lookup_expr='icontains')
    paper_annotation_uz = filters.CharFilter(field_name='paper_annotation_uz', lookup_expr='icontains')
    paper_annotation_en = filters.CharFilter(field_name='paper_annotation_en', lookup_expr='icontains')
    keywords = filters.CharFilter(field_name='keywords', lookup_expr='icontains')

    class Meta:
        model = Papers
        fields = ['paper_title_uz', 'paper_title_en', 'paper_annotation_uz', 'paper_annotation_en', 'keywords']
