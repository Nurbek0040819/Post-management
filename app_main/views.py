from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from app_paper.models import Sphere, Papers
from app_paper.serializers import SphereSerializer, PapersSerializer
from app_publications.models import Publications
from app_publications.serializers import PublicationsSerializer, PublicationsGetSerializer


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response({"error": "Qidiruv parametri kerak"}, status=status.HTTP_400_BAD_REQUEST)

        publications_results = Publications.objects.filter(
            Q(publications_name_uz__icontains=query) |
            Q(publications_name_en__icontains=query)
        )
        publications_serializer = PublicationsSerializer(publications_results, many=True)

        sphere_results = Sphere.objects.filter(
            Q(sphere_name__icontains=query)
        )
        sphere_serializer = SphereSerializer(sphere_results, many=True)

        papers_results = Papers.objects.filter(
            Q(paper_title_uz__icontains=query) |
            Q(paper_title_en__icontains=query) |
            Q(paper_annotation_uz__icontains=query) |
            Q(paper_annotation_en__icontains=query) |
            Q(keywords__icontains=query)
        )
        papers_serializer = PapersSerializer(papers_results, many=True)

        return Response({
            'publications': publications_serializer.data,
            'spheres': sphere_serializer.data,
            'papers': papers_serializer.data
        })


# @api_view(['GET'])
# def main_page(request):
#     last_edition_paper = PublicationsGetSerializer(Publications.objects.all().last())
#
#