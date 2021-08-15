array = [170, 45, 75, 90, 802, 24, 2, 66]


def counting_sort(array, tens):
    # we use a range of 0-9 to sort
    N = 10
    count = [0]*N
    for i in range(len(array)):
        key = (array[i] % tens)//(tens//10)
        count[key] += 1
    for i in range(1, N):
        count[i] = count[i] + count[i-1]
    sorted_array = [0]*len(array)
    for i in range(len(array)-1, -1, -1):
        key = (array[i] % tens)//(tens//10)
        sorted_array[count[key]-1] = array[i]
        count[key] -= 1
    return sorted_array


def radix_sort(array):
    max_val = max(array)
    times = len(str(max_val))
    for i in range(1, times+1):
        array = counting_sort(array, 10**i)
    return array


print("Sorted array =", radix_sort(array))
