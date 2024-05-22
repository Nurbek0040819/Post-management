from django.contrib import admin
from .models import Sphere, Papers

# Register your models here.


@admin.register(Sphere)
class SphereAdmin(admin.ModelAdmin):
    list_display = ('sphere_name',)
    search_fields = ('sphere_name',)


@admin.register(Papers)
class PapersAdmin(admin.ModelAdmin):
    list_display = ('paper_title_uz', 'paper_title_en', 'count_views', 'publication_id')
    search_fields = ('paper_title_uz', 'paper_title_en', 'keywords')
    list_filter = ('paper_sphere', 'publication_id')
    filter_horizontal = ('paper_sphere',)
    readonly_fields = ('count_views',)
    exclude = ('count_views',)
