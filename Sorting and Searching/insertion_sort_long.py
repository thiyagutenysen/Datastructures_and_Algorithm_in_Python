array = [9, 2, 5, 4, 7, 6, 1, 3, 8, 0]


def insertion(array, i, j):
    temp = array[i]
    for k in range(i-1, j-1, -1):
        array[k+1] = array[k]
    array[j] = temp
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        flag = False
        for j in range(i-1, -1, -1):
            if array[i] > array[j]:
                array = insertion(array, i, j+1)
                flag = True
                break
        if flag == False:
            array = insertion(array, i, 0)
    return array


print("Sorted array =", insertion_sort(array))
