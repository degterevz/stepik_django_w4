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
    description = models.TextField(default='')
    employee_count = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=100, default='')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies", null=True)
    skills = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    published_at = models.DateField(null=True)

    class Meta:
        ordering = ['-published_at']


class Application(models.Model):
    written_username = models.CharField(max_length=50)
    written_phone = models.CharField(max_length=30)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')


class Resume(models.Model):
    class Status(models.TextChoices):
        not_looking_for_job = 'NJ', 'Не ищу работу'
        considering_offers = 'CO', 'Рассматриваю предложения'
        looking_for_job = 'LJ', 'Ищу работу'

    class Grade(models.TextChoices):
        intern = 'IN', 'Стажер'
        junior = 'JR', 'Джуниор'
        middle = 'MD', 'Миддл'
        senior = 'SR', 'Синьор'
        lead = 'LD', 'Лид'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume', blank=True,
                             verbose_name='Пользователь')
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, verbose_name='Фамилия')
    status = models.CharField(choices=Status.choices, max_length=30, verbose_name='Готовность к работе')
    salary = models.IntegerField(default=0, verbose_name='Ожидаемое вознаграждение')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resume", null=True,
                                  verbose_name='Специализация')
    grade = models.CharField(choices=Grade.choices, max_length=30, verbose_name='Квалификация')
    education = models.TextField(default='', verbose_name='Образование')
    experience = models.TextField(default='', verbose_name='Опыт работы')
    portfolio = models.CharField(max_length=300, default='', verbose_name='Ссылка на портфолио')
