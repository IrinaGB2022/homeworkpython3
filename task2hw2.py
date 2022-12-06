n = int(input('Введите число : ')) 
def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   

print(f"Список элементов :  {sequence(n)}")
print(f"Сумма элементов списка : {sum(sequence(n))}")