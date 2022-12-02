number = int(input("Введите номер  дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели неверное число! Диапазон вводимых чисел от 1 до 7;)')
elif number > 5:
    print('это выходной!')
else:
    print('нет, это не выходной')

