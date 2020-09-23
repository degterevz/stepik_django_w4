from app_vacancies.models import Specialty, Vacancy


def vacancies_by_specialties():
    """
    Пытался добиться минимального количества запросов к ДБ
    :return: словарь {специализация : вакансии по этой специализации}
    """
    vacancies = dict()
    for specialty in Specialty.objects.all():
        if specialty is not None:
            vacancies[specialty] = []
    for vacancy in Vacancy.objects.select_related():
        if vacancy.specialty is not None:
            vacancies[vacancy.specialty].append(vacancy)
    return vacancies


def vacancies_in_specialty(code):
    """
    Возвращает словарь той же структуры, что и vacancies_by_specialties, только с 1 специализацией.
    (Для возможности использования одного шаблона)
    :param code: код специализации
    :return: словарь {специализация : вакансии по этой специализации}
    """
    vacancies = dict()
    specialty = Specialty.objects.filter(code=code).first()
    vacancies[specialty] = specialty.vacancies.all()
    return vacancies
