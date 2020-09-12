from django.contrib import admin
from django.urls import path

from app_vacancies.views import MainView, VacanciesView, \
    VacanciesCategoryView, VacanciesDetailsView, CompaniesView, custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:category>/', VacanciesCategoryView.as_view(), name='vacancies_category'),
    path('vacancies/<int:id>/', VacanciesDetailsView.as_view(), name='vacancies_details'),
    path('companies/<int:id>/', CompaniesView.as_view(), name='companies_details'),
]

handler404 = custom_handler404
handler500 = custom_handler500
