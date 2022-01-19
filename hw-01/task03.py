# Напишите функцию, печатающую число прописью.
#   Ввод: натуральное число в диапазоне 1..99 включительно.
#   Вывод: соответствующее число прописью на русском языке.
# Перечислять в коде все числа запрещено.

print('Введите число в интервале 1-99')
num = int(input())
if num < 1 or num > 99:
    print('Перезапусти и введи число от 1 до 99 включительно')
    exit()
list_of_uwords = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
                  'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                  'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать']
list_of_dozens = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
                  'восемьдесят', 'девяносто']  # uniq words
dozens = num // 10  # getting dozens from input num
units = num % 10  # getting units from input num


def function(_dozens, _units):
    """
    Getting dozens and units from input value and translating it into a word

    :param _dozens: dozens
    :param _units: units
    :return: word
    """
    # num from 21 to 99 include
    if num >= 21:
        word1 = list_of_dozens[_dozens-1]
        word2 = list_of_uwords[_units-1]
        word = word1 + ' ' + word2
        if num % 10 == 0:
            word = word1
    # num from 1 to  include
    else:
        word = list_of_uwords[num-1]
    return word


print(function(dozens, units))
