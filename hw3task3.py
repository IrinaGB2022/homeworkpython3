#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(i%1,2) for i in my_list]
print(my_list, max(new_list) - min(new_list)) 

my_list = [1.67, 1.84, 3.91, 5, 10.06]
new_list = [round(i%1,2) for i in my_list]
print(my_list, max(new_list) - min(new_list)) 

