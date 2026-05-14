"""Документация модуля игры-тренировки."""
from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name, char_class):
    """Функция атаки."""
    if char_class == 'warrior':
        rand_int = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {rand_int}')
    if char_class == 'mage':
        rand_int = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {rand_int}')
    if char_class == 'healer':
        rand_int = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {rand_int}')


def defence(char_name, char_class):
    """Функция защиты."""
    if char_class == 'warrior':
        rand_int = 10 + randint(5, 10)
        return (f'{char_name} блокировал {rand_int} урона')
    if char_class == 'mage':
        rand_int = 10 + randint(-2, 2)
        return (f'{char_name} блокировал {rand_int} урона')
    if char_class == 'healer':
        rand_int = 10 + randint(2, 5)
        return (f'{char_name} блокировал {rand_int} урона')


def special(char_name, char_class):
    """Функция специального умения."""
    if char_class == 'warrior':
        sum = 80 + 25
        return (f'{char_name} применил специальное умение «Выносливость '
                f'{sum}»')
    if char_class == 'mage':
        sum = 5 + 40
        return (f'{char_name} применил специальное умение «Атака {sum}»')
    if char_class == 'healer':
        sum = 10 + 30
        return (f'{char_name} применил специальное умение «Защита {sum}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name, char_class):
    """Функция начала тренировки."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence'
          ' — чтобы блокировать атаку противника или special — чтобы '
          'использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    """Функция выбора персонажа."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь '
                           'играть: Воитель — warrior, Маг — mage, Лекарь — '
                           'healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и'
                  ' отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким '
                  'интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из '
                  'природы, веры и духов.')
        approve_choice = input(
                       'Нажми (Y), чтобы подтвердить выбор, или любую'
                       ' другую кнопку, чтобы выбрать другого персонажа '
                       ).lower()
    return char_class


# def main(): -> None
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class = choice_char_class()
#     print(start_training(char_name, char_class))


# main()
# ...запишите:
"""Запуск игры-тренировки через конструкцию проверки импорта модуля."""
if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
