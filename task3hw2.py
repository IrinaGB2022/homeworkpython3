list =[5 , 25, 25, 789, 25478, 5476547, 7, 147]
import random
def mix_list(list_base):
    list = list_base[:]
    list_length = len(list)
    for i in range(list_length):
                indexi = random.randint(0, list_length - 1)
                temp = list[i]
                list[i] = list[indexi]
                list[indexi] = temp
                return list

mixed_list = mix_list(list)
print(f"Заданный  список:{list} ")
print(f"Перемешанный  список: {mixed_list}")
