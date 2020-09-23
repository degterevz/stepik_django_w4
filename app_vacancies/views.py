from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, PermissionDenied
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from django.views.generic import CreateView

from app_vacancies.forms import RegisterForm, CompanyForm, VacancyForm, ApplicationForm
from app_vacancies.models import Specialty, Company, Vacancy, Application
from app_vacancies.services import vacancies_by_specialties, vacancies_in_specialty


class MainView(View):
    def get(self, request):
        return render(request, 'index.html', context={
            'specialties': Specialty.objects.all(),
            'companies': Company.objects.all()
        })


class VacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html', context={
            'vacancies_specialties': vacancies_by_specialties()
        })


class VacanciesCategoryView(View):
    def get(self, request, category):
        if not Specialty.objects.filter(code=category).exists():
            raise Http404

        return render(request, 'vacancies.html', context={
            'vacancies_specialties': vacancies_in_specialty(category)
        })


class VacanciesDetailsView(View):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, pk=id)
        return render(request, 'vacancy.html', context={
            'vacancy': vacancy,
            'auth': request.user.is_authenticated
        })


class CompaniesView(View):
    def get(self, request, id):
        company = get_object_or_404(Company, pk=id)
        return render(request, 'company.html', context={
            'company': company
        })


class VacanciesSendApplicationView(LoginRequiredMixin, View):
    """
    View для обработки POST запроса по отклику. Доступен только авторизованным пользователям
    """
    login_url = '/login/'

    def post(self, request, id, *args, **kwargs):
        form = ApplicationForm(request.POST, )

        if form.is_valid():
            form.save()
            return render(request, 'sent.html', context={
                'vacancy_id': request.POST['vacancy']
            })
        else:
            pass


class MyCompanyView(LoginRequiredMixin, View):
    """
    View с разделом компании пользователя. Доступен только авторизованным пользователям.
    """
    login_url = '/login/'

    def get(self, request):
        """
        Если текущий пользователь является владельцем компании, возвращает страницу редактирования компании.
        В противном случае -- с предложением создать новую компанию.
        """
        try:
            company = Company.objects.get(owner__id=request.user.id)
            form = CompanyForm(instance=company)
            return render(request, 'company-edit.html', context={
                'form': form
            })
        except ObjectDoesNotExist:
            return render(request, 'company-create.html')
        except MultipleObjectsReturned:
            raise Http404

    def post(self, request):
        """
        Обработка запроса на создание или редактирование компании.
        """
        try:
            company = Company.objects.get(owner=request.user)

            update = False
            form = CompanyForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                update = True
                form.save()
            return render(request, 'company-edit.html', context={
                'form': form,
                'update': update
            })

        except ObjectDoesNotExist:
            # Создаем компанию с пустыми полями
            Company.objects.create(owner=request.user)
            return render(request, 'company-edit.html')
        except MultipleObjectsReturned:
            raise Http404


class MyVacanciesView(LoginRequiredMixin, View):
    """
    View с разделом вакансий компании пользователя. Доступен только владельцу компании.
    """
    login_url = '/login/'

    def get(self, request):
        """
        Если текущий пользователь является владельцем компании, возвращает страницу со списком вакансий.
        В противном случае -- с предложением создать новую компанию.
        """
        try:
            company = Company.objects.get(owner=request.user)
            vacancies = company.vacancies.all()
            return render(request, 'vacancy-list.html', context={
                'vacancies': vacancies
            })
        except ObjectDoesNotExist:
            return render(request, 'company-create.html')
        except MultipleObjectsReturned:
            raise Http404

    def post(self, request):
        """
        Обработка запроса на создание новой вакансии.
        """
        try:
            company = Company.objects.get(owner=request.user)
            vacancy = Vacancy.objects.create(company=company, published_at=datetime.today())
            return redirect('my_vacancy', id=vacancy.id)
        except ObjectDoesNotExist:
            return render(request, 'company-create.html')
        except MultipleObjectsReturned:
            raise Http404


class MyVacancyView(LoginRequiredMixin, View):
    """
    View с разделом одной вакансии компании пользователя. Доступен только владельцу компании.
    """
    login_url = '/login/'

    def get(self, request, id):
        """
        Если вакансии не существует - 404.
        Если пользователь не является владельцем компании вакансии - ошибка доступа.
        """
        try:
            vacancy = Vacancy.objects.get(id=id)
            applications = Application.objects.filter(vacancy=id)

            if vacancy.company.owner_id == request.user.id:
                form = VacancyForm(instance=vacancy)
                return render(request, 'vacancy-edit.html', context={
                    'form': form,
                    'applications': applications
                })
            else:
                raise PermissionDenied
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Http404

    def post(self, request, id):
        """
        Обработка запросов на изменение вакансии.
        Если вакансии не существует - 404.
        Если пользователь не является владельцем компании вакансии - ошибка доступа.
        """
        try:
            vacancy = Vacancy.objects.get(id=id)
            if vacancy.company.owner.id == request.user.id:
                form = VacancyForm(request.POST, instance=vacancy)

                if form.is_valid():
                    form.save()
                    update = True
                else:
                    update = False

                applications = Application.objects.filter(vacancy=id)
                return render(request, 'vacancy-edit.html', context={
                    'form': form,
                    'applications': applications,
                    'update': update
                })
            else:
                raise PermissionDenied
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Http404


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    redirect_field_name = 'next'
    template_name = 'login.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = '/login'
    template_name = 'register.html'


class MyLogoutView(LogoutView):
    pass


class SearchView(View):
    def get(self, request):
        try:
            query = request.GET['s']
            vacancies = Vacancy.objects.filter(title__contains=query)
            # В sqlite3 не работает поиск без учета регистра :(
            return render(request, 'search.html', context={
                'vacancies': vacancies,
                'query': query
            })
        except MultiValueDictKeyError:
            raise Http404


# проверил


class MyResumeView(View):
    pass


def custom_handler403(request, exception):
    return HttpResponseForbidden(render_to_string('access-error.html'))


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!(404)')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините!(500)')
