from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app_vacancies.views import (
    MainView,
    VacanciesView,
    VacanciesCategoryView,
    VacanciesDetailsView,
    CompaniesView,
    VacanciesSendApplicationView,
    MyCompanyView,
    MyVacanciesView,
    MyVacancyView,
    MyLoginView,
    RegisterView,
    MyLogoutView,
    custom_handler404,
    custom_handler500, custom_handler403, SearchView, MyResumeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:category>/', VacanciesCategoryView.as_view(), name='vacancies_category'),
    path('vacancies/<int:id>/', VacanciesDetailsView.as_view(), name='vacancies_details'),
    path('companies/<int:id>/', CompaniesView.as_view(), name='companies_details'),

    path('vacancies/<int:id>/send/', VacanciesSendApplicationView.as_view(), name='vacancy_send'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:id>/', MyVacancyView.as_view(), name='my_vacancy'),

    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

    path('search/', SearchView.as_view(), name='search'),
    path('myresume/', MyResumeView.as_view(), name='my_resume')
]

handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)