from app_vacancies.models import Specialty, Vacancy


def vacancies_by_specialties():
    """
    Пытался добиться минимального количества запросов к ДБ
    :return: словарь {специализация : вакансии по этой специализации}
    """
    data = dict()
    for specialty in Specialty.objects.all():
        data[specialty] = []

    for vacancy in Vacancy.objects.select_related():
        data[vacancy.specialty].append(vacancy)
    return data


def vacancies_in_specialty(code):
    """
    Возвращает словарь той же структуры, что и vacancies_by_specialties, только с 1 специализацией.
    (Для возможности использования одного шаблона)
    :param code: код специализации
    :return: словарь {специализация : вакансии по этой специализации}
    """
    data = dict()
    specialty = Specialty.objects.filter(code=code).first()
    data[specialty] = specialty.vacancies.all()
    return data
