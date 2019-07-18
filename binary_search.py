def binary_search(list,item):
    low = 0
    hight = len(list)-1

    while low <= hight:
        mid = (low + hight)//2      # => пока эта часть не сократится до одного элемента - проверяем средний элемент
        guess = list[mid]
        if guess == item:           # => значение найдено
            return mid
        if guess > item:            # => много
            hight = mid-1
        else:                       # => мало
            low = mid+1
    return None                     # => значение не существует

                                    # => протестируем функцию
my_list = [1, 3, 5, 7, 9, 23, 54, 55, 56, 89, 99]

print(binary_search(my_list, 5))    # => 2
print(binary_search(my_list, 57))   # => None