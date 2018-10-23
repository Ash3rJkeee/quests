"""Задача описания механизма заполнения водой любой лужи"""

from random import *


class Cavity:
    """Класс Полость"""

    def __init__(self, num):
        self.h = randint(0, H - 1)       # координата дна текущей полости относительно самой глубокой
        self.v = 0                       # заполнение полости над h
        self.w = self.h                  # уровень воды в полости
        self.number = num                # уникальный номер полости

    def add(self):
        """функция добавления воды в полость"""
        print()
        print('Добавление воды в полость №', self.number)

        # флаг, т.к. вложенный if питон в этом месте не обрабатывал корректно
        flag = True

        # проверка на случай равенства уровня воды во всех полостях
        equal = 0
        j = 0
        while j < len(L) - 1:
            if L[j].w == L[j + 1].w:
                equal = equal + 1
            j = j + 1

        if equal == 0:
            L[0].v = L[0].v + 1
            L[0].w = L[0].h + L[0].v
            flag = False

        try:
            if (self.w >= L[self.number - 1].w) and flag:
                print('Сравнение слева :', L[self.number - 1].w, self.w)
                L[self.number - 1].add()
                flag = False
        except IndexError:
            pass

        try:
            if (self.w > L[self.number + 1].w) and flag:
                print('Сравнение справа :', self.w, L[self.number + 1].w)
                L[self.number + 1].add()
                flag = False
        except IndexError:
            pass

        if flag:
            if self.w < H:
                self.v = self.v + 1
                self.w = self.h + self.v
            else:
                """Обработка, если уперлись в верх лужи. Поиск полости вширь."""
                print("Уперлись в верхний уровень")
                flag2 = True
                k = 0
                while flag2:
                    k = k + 1
                    try:
                        if H - L[self.number - k].w > 0:
                            flag2 = False
                            L[self.number - k].add()
                            break
                    except IndexError:
                        pass

                    try:
                        if (H - L[self.number + k].w) > 0:
                            flag2 = False
                            L[self.number + k].add()
                            break
                    except IndexError:
                        pass
                    if k == N:
                        break


def print_puddle():
    """вывод на печать формы лужи"""
    global H, N, L
    print(" - - - - - ")
    for row in range(H, -1, -1):
        string = ""
        for col in range(N):
            if row <= L[col].h:
                string = string + " 0"
            elif (row > L[col].h) and (row <= L[col].w):
                string = string + " 1"
            else:
                string = string + "  "
        print(string)
    print()


"""описание лужи"""
H = int(input('Введите глубину лужи: '))  # максимальная глубина лужи


# количество полостей в луже
N = int(input("введите количество полостей: "))

"""Создаем лужу"""
L = []  # массив полостей
V = 0   # вмещаемый суммарный объем
for i in range(N):
    L.append(Cavity(i))
    print('Высота дна: ', L[i].h, ", номер полости ", L[i].number)
    V = V + (H - L[i].h)

print()
print("Сгенерировалась такая лужа: ")
print_puddle()

print()

income = int(input('введите, в какую полость лить воду: '))
sum_v = 0

while sum_v < V:
    input("Нажми Enter для следующего шага")
    sum_v = 0
    L[income].add()
    for i in L:
        sum_v = sum_v + i.v
    print_puddle()
    print("sum_v = ", sum_v)

print("Моделирование закончено")
