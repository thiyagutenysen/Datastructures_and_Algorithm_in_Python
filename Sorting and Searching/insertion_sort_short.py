array = [9, 2, 5, 4, 7, 6, 1, 3, 8, 0]


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while(j >= 0 and key < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


print("Sorted array =", insertion_sort(array))
