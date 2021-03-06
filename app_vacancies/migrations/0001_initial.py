# Generated by Django 3.1.1 on 2020-09-24 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('logo', models.ImageField(height_field='height_field', upload_to='company_images', width_field='width_field')),
                ('height_field', models.PositiveIntegerField(default=0)),
                ('width_field', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('employee_count', models.IntegerField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('picture', models.ImageField(height_field='height_field', upload_to='speciality_images', width_field='width_field')),
                ('height_field', models.PositiveIntegerField(default=0)),
                ('width_field', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('skills', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.TextField(default='')),
                ('salary_min', models.IntegerField(default=0)),
                ('salary_max', models.IntegerField(default=0)),
                ('published_at', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='app_vacancies.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='app_vacancies.specialty')),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('surname', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('status', models.CharField(choices=[('NJ', 'Не ищу работу'), ('CO', 'Рассматриваю предложения'), ('LJ', 'Ищу работу')], max_length=30, verbose_name='Готовность к работе')),
                ('salary', models.IntegerField(default=0, verbose_name='Ожидаемое вознаграждение')),
                ('grade', models.CharField(choices=[('IN', 'Стажер'), ('JR', 'Джуниор'), ('MD', 'Миддл'), ('SR', 'Синьор'), ('LD', 'Лид')], max_length=30, verbose_name='Квалификация')),
                ('education', models.TextField(default='', verbose_name='Образование')),
                ('experience', models.TextField(default='', verbose_name='Опыт работы')),
                ('portfolio', models.CharField(default='', max_length=300, verbose_name='Ссылка на портфолио')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='app_vacancies.specialty', verbose_name='Специализация')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=50)),
                ('written_phone', models.CharField(max_length=30)),
                ('written_cover_letter', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='app_vacancies.vacancy')),
            ],
        ),
    ]
