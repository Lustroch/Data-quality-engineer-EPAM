# В этой задаче вам необходимо создать объектную модель лыжника, спускающегося с горы.

# Лыжник может спускаться с горы в произвольном направлении. Однако для определенности положим, что он может
# перемещаться только в 3-х направлениях: Юг, Запад, Восток.

# При этом, если он идет галсами в направлении Запад или Восток, то его скорость составляет 1 м/с, а если катится прямо
# вниз (Юг), то скорость выше, и равна 5 м/с.

# Создайте программную модель движения лыжника и определите:
# 1) какое расстояние он проедет через 17 секунд спуска, если каждую секунду он меняет направление движения случайным
# образом,
# и
# 2) в каком направлении он двигался каждую секунду.

# Приложение должно состоять из двух классов. Первый класс наполните характеристиками и методами лыжника. Второй класс
# используйте для параметров движения. Управление программой и вывод результатов производите в основной функции main.

import random


class Directions:

    def __init__(self, tacks, straight):
        self.tacks = tacks
        self.straight = straight

    def west_east(self):
        return self.tacks

    def south(self):
        return self.straight


class Skier:

    def __init__(self, name):
        self.name = name

    def ski_run(self, seconds):
        directions = ['south', 'west', 'east']  # list of directions
        distance = 0
        for i in range(1, seconds + 1):
            dir = directions[random.randint(0, len(directions)-1)]
            if dir == ('west' or 'east'):
                distance += Directions.west_east(speed_of_directions)
            else:
                distance += Directions.south(speed_of_directions)
            print(i, 'second direction was', dir)
        print('Total distance is ', distance)


speed_of_directions = Directions(1, 5)
michel = Skier('Michel')
michel.ski_run(17)
