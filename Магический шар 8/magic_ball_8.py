from random import *


def magic_ball():
    Positive = [
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо да",
        "Можешь быть уверен в этом",
    ]
    Hesitantly_positive = [
        "Мне кажется - да",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят - да",
        "Да",
    ]
    Neutral = [
        "Пока неясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять",
    ]
    Negative = [
        "Даже не думай",
        "Мой ответ - нет",
        "По моим данным - нет",
        "Перспективы не очень хорошие",
        "Весьма сомнительно",
    ]
    answ = choice([Positive, Hesitantly_positive, Neutral, Negative])
    print(choice(answ))


def again():
    print("Хотите задать еще вопрос?")
    if input().lower() in ["lf", "да"]:
        question()
    else:
        print("Возвращайся если возникнут вопросы!")


def question():
    que = input("Введите вопрос: ")
    print("Волшебный шар дал свой ответ...")
    magic_ball()
    again()


print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Введите свое имя: ")
print("Привет ", name.capitalize())
question()
