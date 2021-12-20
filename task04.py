grandma = 'Бабушка, бабушка, купим '  # calling grandma
an = ['курочку', 'уточку', 'индюшонка', 'кисоньку', 'собачонку', 'коровёнку', 'поросёнка']  # list of the animals
ans = ['Курочка по зёрнышку кудах-тах-тах. \n', 'Уточка та-ти-та-та, \n', 'Индюшонок фалды-балды, \n',
       'А кисуня мяу-мяу, \n', 'Собачонка гав-гав, \n', 'Коровёнка муки-муки, \n',
       'поросёнка - Поросёнок хрюки-хрюки, \n']  # list of the animal's sounds
lst2 = 'Бабушка, бабушка, купим телевизор! \n'  # suggesting to buy a TV to grandma
lst1 = 'Телевизор надо, надо, ведь у нас такое стадо! \n'  # a joke about number of animals
# output 8 couplets
for i in range(7):
    # calling grandma to buy someone twice
    for j in range(2):
        print(grandma, an[i] + '!')
    # repeating sounds of the current animal and the previous ones
    for k in range(i + 1, 0, -1):
        counter = k - 1
        print(ans[counter], end='')
        counter -= 1
    print()
    counter = 0
# calling grandma to buy a TV for some reason
for b in range(2):
    print(lst2, end='')
print(lst1)
