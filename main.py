import application.salary as salary
import application.db.people as people
import datetime
 # доп. модуль из pip
from pynames import GENDER, LANGUAGE
from pynames.generators.elven import DnDNamesGenerator

# генерация имени
def print_generate_name():
    print('Генерация мужского имени:')
    elven_generator = DnDNamesGenerator()
    name = elven_generator.get_name(GENDER.MALE)
    print(name)

    translation = name.translations
    print(translation)


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(f'Текущее время: {datetime.datetime.now()}')

    print_generate_name()

