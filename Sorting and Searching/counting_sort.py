array = [9, 2, 5, 4, 7, 6, 1, 3, 8, 0]


def counting_sort(array):
    # we use a range of 0-9 to sort
    N = 10
    count = [0]*N
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(1, N):
        count[i] = count[i] + count[i-1]
    sorted_array = [0]*len(array)
    for i in range(len(array)-1, -1, -1):
        sorted_array[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
    return sorted_array


print("Sorted array =", counting_sort(array))
