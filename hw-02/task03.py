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

import random


class Skier:

    def __init__(self, speed_tacks, speed_straight):
        self.st = speed_tacks
        self.ss = speed_straight

    def random_distance(self, seconds):
        l_of_dir = ['south', 'west', 'east']  # list of directions
        distance = 0
        for i in range(1, seconds + 1):
            dir = l_of_dir[random.randint(0, len(l_of_dir)-1)]
            if dir == ('west' or 'east'):
                distance += self.st
            else:
                distance += self.ss
            print(i, 'second direction was', dir)
        print('Total distance is ', distance)


michel = Skier(1, 5)
michel.random_distance(17)
