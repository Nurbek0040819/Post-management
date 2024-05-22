from django.db import models

from app_journal.models import AbstractBaseModel


# Create your models here.


class Sphere(models.Model):
    sphere_name = models.CharField(max_length=45)


class Papers(AbstractBaseModel):
    paper_sphere = models.ManyToManyField(Sphere)
    paper_title_uz = models.CharField(max_length=255)
    paper_title_en = models.CharField(max_length=255)
    paper_annotation_uz = models.TextField()
    paper_annotation_en = models.TextField()
    count_views = models.IntegerField(default=0)
    paper_references = models.URLField()
    keywords = models.TextField()
    publication_id = models.ForeignKey('app_publications.Publications', on_delete=models.CASCADE)


class Reviewers(models.Model):
    full_name = models.CharField(max_length=45)
    position_uz = models.CharField(max_length=150)
    position_en = models.CharField(max_length=150)
    sphere_id = models.ManyToManyField(Sphere)


class Feedback(models.Model):
    paper_id = models.ForeignKey(Papers, on_delete=models.CASCADE)
    Reviewer_id = models.ForeignKey(Reviewers, on_delete=models.CASCADE)
    file = models.FileField(upload_to='feedback/')
