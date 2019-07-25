def countdown(i):   #счет с помощью рекурсии
    print (i)
    if i <= 1:
        return
    else:
        countdown(i-1)

countdown (3)

def sum(list):   #суммирование элементов массива с помощью рекурсии
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print (sum([2,5,2,4,1]))

def count(list):   #нахождение количества элементов массива с помощью рекурсии
    if list == []:
        return 0
    return 1 + count(list[1:])

print (count([2,5,2,4,1]))

def max(list): #нахождение максимального элемента массива с помощью рекурсии
    if len(list) == 2:
        return list[0] if list[0]>list[1] else list[1]
    return list[0] if list[0]>max(list[1:]) else max(list[1:])

print (max([2,5,7,4,1]))