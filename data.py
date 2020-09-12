""" Вакансии """
jobs = [
    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-14", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-04-17", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-9", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-1", "desc": "Потом добавим"},
    {"title": "Фронтендер в проект", "cat": "frontend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-12", "desc": "Потом добавим"},
    {"title": "Фронтендер в стартап", "cat": "frontend", "company": "workiro", "salary_from": "100000",
     "salary_to": "120000", "posted": "2020-03-11", "desc": "Потом добавим"}
]

""" Компании """
companies = [
    {"title": "workiro", "location": "Москва", "employee_count": "120"},
    {"title": "rebelrage", "location": "Санкт-Петербург", "employee_count": "100"},
    {"title": "staffingsmarter", "location": "Москва", "employee_count": "80"},
    {"title": "evilthreath", "location": "Рязань", "employee_count": "65"},
    {"title": "hirey", "location": "Красноярск", "employee_count": "180"},
    {"title": "swiftattack", "location": "Новосибирск", "employee_count": "15"},
    {"title": "troller", "location": "Иваново", "employee_count": "10"},
    {"title": "primalassault", "location": "Казань", "employee_count": "5"}
]

""" Категории """

specialties = [
    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"}
]

""" Статусы в формате Enum """

#
#
# class EducationChoices(Enum):
#     missing = 'Отсутствует'
#     secondary = 'Среднее'
#     vocational = 'Средне-специальное'
#     incomplete_higher = 'Неполное высшее'
#     higher = 'Высшее'
#
#
# class GradeChoices(Enum):
#     intern = 'intern'
#     junior = 'junior'
#     middle = 'middle'
#     senior = 'senior'
#     lead = 'lead'
#
#
# class SpecialtyChoices(Enum):
#     frontend = 'Фронтенд'
#     backend = 'Бэкенд'
#     gamedev = 'Геймдев'
#     devops = 'Девопс'
#     design = 'Дизайн'
#     products = 'Продукты'
#     management = 'Менеджмент'
#     testing = 'Тестирование'
#
#
# class WorkStatusChoices(Enum):
#     not_in_search = 'Не ищу работу'
#     consideration = 'Рассматриваю предложения'
#     in_search = 'Ищу работу'
