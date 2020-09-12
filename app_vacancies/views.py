from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.views import View

from app_vacancies.models import Specialty, Company, Vacancy
from app_vacancies.services import vacancies_by_specialties, vacancies_in_specialty


class MainView(View):
    def get(self, request):
        return render(request, 'index.html', {'specialties': Specialty.objects.all(),
                                              'companies': Company.objects.all()})


class VacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html',
                      context={'vacancies_specialties': vacancies_by_specialties()})


class VacanciesCategoryView(View):
    def get(self, request, category):
        if len(Specialty.objects.filter(code=category)) == 0:
            raise Http404

        return render(request, 'vacancies.html',
                      context={'vacancies_specialties': vacancies_in_specialty(category)})


class VacanciesDetailsView(View):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, pk=id)
        return render(request, 'vacancy.html', context={'vacancy': vacancy})


class CompaniesView(View):
    def get(self, request, id):
        company = get_object_or_404(Company, pk=id)
        return render(request, 'company.html', context={'company': company})


class VacanciesSendApplicationView(View):
    def get(self, request, id):
        pass


class MyCompanyView(View):
    def get(self, request):
        pass


class MyVacanciesView(View):
    def get(self, request):
        pass


class MyVacancyView(View):
    def get(self, request):
        pass


class LoginView(View):
    def get(self, request):
        pass


class RegisterView(View):
    def get(self, request):
        pass


class LogoutView(View):
    def get(self, request):
        pass




def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!(404)')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!(500)')
