from functools import cmp_to_key


def largestNumber(A):
    A = map(str, A)
    key = cmp_to_key(lambda a, b: 1 if a+b >= b+a else -1)
    res = ''.join(sorted(A, key=key, reverse=True))
    print(res)
    return 0


A = [3, 30, 34, 5, 9]
print(largestNumber(A))
