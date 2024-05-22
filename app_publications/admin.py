from django.contrib import admin
from .models import Publications

# Register your models here.


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('publications_name_uz', 'publications_name_en')
    search_fields = ('publications_name_uz', 'publications_name_en')
    filter_horizontal = ('include_sphere',)
