from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_model'


class Contact(models.Model):
    first_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='contacts')
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.first_name} - {self.email} - {self.message}"

    class Meta:
        db_table = 'contacts'
        verbose_name_plural = 'Contacts'


class FAQ(models.Model):
    question_uz = models.CharField(max_length=255)
    question_eng = models.CharField(max_length=255)
    answer_uz = models.CharField(max_length=255)
    answer_eng = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question_uz} - {self.answer_uz}"

    class Meta:
        db_table = 'faq'
        verbose_name_plural = 'faq'


class Requirements(AbstractBaseModel):
    title_uz = models.CharField(max_length=255)
    title_eng = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_eng = models.TextField()

    def __str__(self):
        return f"{self.title_uz} - {self.description_uz}"

    class Meta:
        db_table = 'requirements'
        verbose_name_plural = 'Requirements'
