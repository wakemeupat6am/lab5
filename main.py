import random

def prog1():

    a = [random.randint(1, 10) for i in range(5)]

    b = int(input('Введите число:'))

    if b in a:

        print("Поздравляю, Вы угадали число!")

    else:

        print("Нет такого числа!")

    print('Были загаданы числа:', a)


def prog2():

    a = [random.randint(1, 10) for i in range(5)]

    print(a)

    for idx in range(len(a)):
        element1 = a[idx]
        for idx2 in range(idx + 1, len(a)):
            element2 = a[idx2]
            if element1 == element2:
                print(element1)
                return


def prog3():
    days = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")

    daysoff = int(input('Колво выходных:'))

    weekends_start_index = len(days) - daysoff
    weekends = days[weekends_start_index:len(days)]
    workdays = days[0:weekends_start_index]

    print("Ваши выходные дни: ", weekends)
    print("Рабочие дни: ", workdays)


def prog4():

    from random import shuffle

    group1 = ["Алиева", "Аузяк", "Ахмедов", "Беликова", "Бигалиев", "Васильев", "Гумерова", "Гусев", "Ефлютина",
              "Жарко"]
    group2 = ["Бабушкин", "Голяев", "Иванов", "Ирматов", "Коровашев", "Насулина", "Нуратдинов", "Ольховский", "Рубцова"]

    shuffle(group1)
    shuffle(group2)

    group1_team = group1[0:5]
    group2_team = group2[0:5]

    team = group1_team + group2_team

    print("Первая группа", group1, "\nВторая группа", group2)
    print("Новая команда", team, "\nДлина", len(team))

    team.sort()

    print("По алфавиту", team)

    if "Иванов" in team:
        print("Иванов есть в команде")

    ivanov_count = team.count("Иванов")
    print("Иванов встречается раз", ivanov_count)

prog1()
prog2()
prog3()
prog4()