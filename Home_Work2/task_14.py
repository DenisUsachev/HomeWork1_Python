#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('До какой степень хотите увидеть результат: ')) 

for i in range(1, number + 1):
    print(2 ** i)