def findSmallest(arr): # находим самый маленький элемент в массиве (списке), возвращаем его индекс
    smallest = arr [0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): # находим индекс самого маленького элемента в списке с помощью функции findSmallest(arr). Возвращаем и удаляем этот элемент из массива arr и добавляем его в новый сортированный массив newArr
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) # Метод .append(x) добавляет элемент 'x' в конец списка. Метод .pop([i]) удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
    return newArr

my_arr = [9, 6, 9, 3, 7]
print (selectionSort(my_arr))