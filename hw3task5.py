#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов 
# (Негафибоначчи).


n = int(input('Введите число: '))

def get_fibon(n):
    fibo_number = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_number.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_number.insert(0, a)
        a, b = b, a - b
    return fibo_number

fibo_numb = get_fibon(n)
print(get_fibon(n))
