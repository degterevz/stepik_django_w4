from data import jobs, companies, specialties
from app_vacancies.models import Vacancy, Company, Specialty

picture_url = 'https://place-hold.it/100x60'


def load():
    for specialty in specialties:
        Specialty.objects.create(code=specialty['code'], title=specialty['title'],
                                 picture=picture_url)

    for company in companies:
        Company.objects.create(name=company['title'], location=company['location'],
                               employee_count=company['employee_count'], logo=picture_url)

    for job in jobs:
        specialty = Specialty.objects.get(code=job['cat'])
        company = Company.objects.get(name=job['company'])

        Vacancy.objects.create(title=job['title'], specialty=specialty, company=company, description=job['desc'],
                               salary_min=job['salary_from'], salary_max=job['salary_to'],
                               published_at=job['posted'])
