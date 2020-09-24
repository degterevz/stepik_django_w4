from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from app_vacancies.models import Company, Vacancy, Application, Resume


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'location', 'employee_count', 'description']


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

        # включаем стили
        self.helper.span = False
        self.helper.label_class = 'mb-2 text-dark'


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name',
            'surname',
            'status',
            'salary',
            'specialty',
            'grade',
            'education',
            'experience',
            'portfolio',
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

        # включаем стили
        self.helper.span = False
        self.helper.label_class = 'mb-2 text-dark'