sum = 0
input_num = input('Введите вещественное  число: ')

for i in input_num:
    if i.isdigit():
        sum += int(i)

print(sum)