# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')
        hero._experience += 50
        print('Вы получаете 50 опыта')
        hero.level_up()

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш уровень:', hero._level, 'Ваш накопленный опыт:', hero._experience + (hero._level - 1) * 150)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('DDDDDD    RRRRRR      AA        GGGGG        OOO      N      N    SSSSS ')
        print('D     D   R     R    A  A      G     G     OO   OO    NN     N  S      S')
        print('D      D  R     R   A    A    G       G   O       O   N N    N  S       ')
        print('D      D  R     R  A      A  G           O         O  N  N   N   SSS    ')
        print('D      D  RRRRRR   A      A  G           O         O  N   N  N      SSS ')
        print('D      D  RR       AAAAAAAA  G     GGGG  O         O  N    N N         S')
        print('D      D  R RR     A      A  G        G   O       O   N     NN         S')
        print('D     D   R   RR   A      A   G      G     OO   OO    N      N  S      S')
        print('DDDDDD    R    RR  A      A    GGGGGG        OOO      N      N   SSSSSS ')
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        
        hero = Hero(input())

        dragon_number = randint(1,5)
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == dragon_number)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
