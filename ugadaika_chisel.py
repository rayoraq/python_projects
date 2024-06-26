# Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
from random import *
def replay():
    if input('Замечачельно!!! Хотите ли сыграть еще раз? ').lower() in ['lf','да','ryi','кнш']:
        start()
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")



def game(a_1,a_2):
    alternative_many = ['Ох, слишком много! Попробуй еще раз', 'Ого-го, это слишком много!',
                        'Много!', 'Многовато!', 'Нужно меньшее число!']
    alternative_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато!', 'Эх, это слишком мало!',
                        'Мало!', 'Надо больше!', 'Нужно большее число!']
    alternative_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
                      'Горячо!']
    alternative_guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
    if a_1 > a_2:
        a_1, a_2 = a_2, a_1
    if a_1 < a_2:
        Chislo = randint(a_1, a_2)
        flag = False
        count=0
        while flag == False:
            popitka = input(f"Угадайте число из диапазона от {a_1} до {a_2}: ")
            if popitka.isdigit()==False:
                while popitka.isdigit()==False:
                    popitka=input(f"Введите ЧИСЛО из диапазона от {a_1} до {a_2}:")
            count+=1
            popitka=int(popitka)
            if a_1<=popitka<=a_2:
                if abs(popitka-Chislo)<=5 and popitka!=Chislo:
                    print(choice(alternative_almost))
                if popitka < Chislo:
                    print(choice(alternative_little))
                if popitka > Chislo:
                    print(choice(alternative_many))
                if popitka==Chislo:
                    flag = True
                    print(choice(alternative_guessed))
                    print(f"Вы угадали загаданное чмсло с {count} попытки")
            else:
                print('Введенное число вне диапазона')
    replay()

def game_rules():
    print('Отлично! Давай ознакомлю тебя с правилами игры.')
    print('Я загадаю число, а ты будешь его отгадывать.')
    print('Диапазон чисел ты выберешь сам.')
    print('К примеру, если ты укажешь диапазон чисел от 0 до 100, я не смогу загадать число "101".')
    print('Я попрошу тебя ввести границы диапазона. Границы не должны совпадать! Так играть мы не сможем.')
    print("Давай начинать!")
    start()

def intro():
    print("Привет!")
    print("Добро пожаловать в числовую угадайку")
    da = input('Если хочешь сыграть, введи слово "да": ')
    if da.lower() in ['да','lf']:
        rules = input('Хочешь узнать правила? ')
        if rules.lower() in ['да','lf']:
            game_rules()
        else:
            start()
    else:
        print("Хорошо, в следующий раз")

def check_a_1(a_1):
    if a_1.isdigit()==False:
        alternative = ['Давай попробуем снова, введи число', 'Это не число, давай с начала']
        print(choice(alternative))
        start()

def check_a_1_a_2(a_1,a_2):
    if a_2.isdigit()==False:
        alternative = ['Давай попробуем снова, введи число', 'Это не число, давай с начала']
        print(choice(alternative))
        start()
    if a_1 == a_2:
        print("Ты ввел одинаковые значения, давай попробуем снова")
    else:
        return True

def start():
    a_1 = input("Введите первую границу диапазона: ")
    check_a_1(a_1)
    a_2 = input("Введите вторую границу диапазона: ")
    check_a_1_a_2(a_1,a_2)
    if check_a_1_a_2(a_1,a_2) ==True:
        a_1,a_2=int(a_1),int(a_2)
        game(a_1,a_2)

intro()