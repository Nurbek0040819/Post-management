from django.db import models


# Create your models here.


class Publications(models.Model):
    publications_name_uz = models.CharField(max_length=255)
    publications_name_en = models.CharField(max_length=255)
    pub_image = models.ImageField(upload_to='publications/')
    pub_file_uz = models.FileField(upload_to='publications/file-uz')
    pub_file_en = models.FileField(upload_to='publications/file-en')
    include_sphere = models.ManyToManyField('app_paper.Sphere')
