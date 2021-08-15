array = [9, 2, 5, 4, 7, 6, 1, 3, 8, 0]


def merge(array, low, mid, high):
    helper = array[low:high]
    left = 0
    right = mid-low
    holder = low
    while(left < mid-low and right < high-low):
        if helper[left] < helper[right]:
            array[holder] = helper[left]
            left += 1
        else:
            array[holder] = helper[right]
            right += 1
        holder += 1
    if left < mid-low:
        for i in range(left, mid-low):
            array[holder] = helper[i]
            holder += 1


def merge_sort(array, low=0, high=len(array)):
    if high-low >= 2:
        mid = (low + high)//2
        merge_sort(array, low, mid)
        merge_sort(array, mid, high)
        merge(array, low, mid, high)


merge_sort(array)
print(array)
