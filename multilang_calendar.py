# --------------------------- Homework_8  ------------------------------------

"""

Виконав: Григорій Чернолуцький

Homework_8

Для функції get_data(), яка повертає список днів тижня
Створіть два декоратори:

Декоратор_№1 / Обов'язковий/ short_form -> повертає скорочення днів тижня
приклад:
Коли get_data() має значення ['Monday', ..., 'Sunday'], тоді декоратор
short_form має повертати ['Mon', ..., 'Sun'].
*** Порада: знайдіть модуль `calendar` та функцію, яка підходить саме Вам.

Декоратор_№2 / Додатковий / translate(language) -> декоратор, який приймає аргумент «language».
Має перекласти назви днів тижня на мову, вказану в параметрі.
*** Порада: дізнайтеся, як працює модуль `locale`, і знайдіть функцію `setlocale`.
Ви можете вільно використовувати будь-яке інше рішення перекладу

В результаті програма повинна просто вивести на екран список, наприклад, німецькомовних скорочень днів тижня. ->
['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

Декоратори та головні виклики мають бути в різних модулях!
Бажано передбачити створення та використання віртуального оточення.

Package Version
------- -------
pip 24.3.1

"""

import locale
import calendar
from functools import wraps


def short_form(func):
    @wraps(func)
    def wrapper():
        return list(calendar.day_abbr)

    return wrapper


def translate(locale_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Зберегаємо поточну локаль
            current_locale = locale.getlocale(locale.LC_TIME)
            try:
                # Встановлюємо потрібну локаль
                locale.setlocale(locale.LC_TIME, locale_name)
                result = func(*args, **kwargs)
            finally:
                # Встановлюємо локаль що була раніше
                locale.setlocale(locale.LC_TIME, current_locale)
            return result

        return wrapper

    return decorator


@translate("de_DE.utf8")
@short_form
def get_data():
    return list(calendar.day_name)
