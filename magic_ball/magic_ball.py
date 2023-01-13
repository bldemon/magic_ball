import random


def choice(n):
    answer = ("Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
              "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
              "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
              "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
              "Перспективы не очень хорошие", "Весьма сомнительно")
    match n:
        case 1: return answer[0]
        case 2: return answer[1]
        case 3: return answer[2]
        case 4: return answer[3]
        case 5: return answer[4]
        case 6: return answer[5]
        case 7: return answer[6]
        case 8: return answer[7]
        case 9: return answer[8]
        case 10: return answer[9]
        case 11: return answer[10]
        case 12: return answer[11]
        case 13: return answer[12]
        case 14: return answer[13]
        case 15: return answer[14]
        case 16: return answer[15]
        case 17: return answer[16]
        case 18: return answer[17]
        case 19: return answer[18]
        case 20: return answer[19]


print('Добро пожаловать в магический шар')
print('Как вас зовут:')
name = input()
flag = True

while flag:
    print(name, 'задайте вопрос магическому шару:')
    input()
    num = random.randint(1, 20)
    print(choice(num))
    print('Если хотите задать еще вопрос, нажмите 1')
    cont_game = input()
    if cont_game in '1':
        continue
    else:
        print('Спасибо за вопросы.')
        flag = False
