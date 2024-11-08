# --------------------------- Homework_8  ------------------------------------

"""

Виконав: Григорій Чернолуцький

Homework_8

Для функції get_data(), яка повертає список днів тижня
Створіть два декоратора:

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
Бажано передбачити ствоерення та використання віртуального оточення.

"""


import calendar
import locale
from functools import wraps

#@translate("de_DE.utf8")
# @short_form
def get_data():
    return list(calendar.day_name)



