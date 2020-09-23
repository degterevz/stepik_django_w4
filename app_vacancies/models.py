from django.contrib.auth.models import User
from django.db import models

from vacancies.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR,
                                height_field='height_field', width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR,
                             height_field='height_field', width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    employee_count = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, default='')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies", null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies", null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True, default='')
    description = models.TextField(null=True, blank=True, default='')
    salary_min = models.IntegerField(default=0, blank=True)
    salary_max = models.IntegerField(default=0, blank=True)
    published_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at']


class Application(models.Model):
    written_username = models.CharField(max_length=50)
    written_phone = models.CharField(max_length=30)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', null=True)
