array = [2, 24, 45, 66, 75, 90, 170, 802]


def binary_search(array, x, low=0, high=len(array)):
    if low >= high:
        return False
    mid = (low+high)//2
    if array[mid] == x:
        return True
    elif array[mid] < x:
        return binary_search(array, x, mid+1, high)
    else:
        return binary_search(array, x, low, mid)


print(binary_search(array, 803))
