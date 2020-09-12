from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=100)
    description = models.TextField()
    employee_count = models.IntegerField(null=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    class Meta:
        ordering = ['-published_at']
