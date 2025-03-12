def check(arr, n, k, l, mid):
    operations = 0
    i = 0
    while i < n:
        if arr[i] < mid:
            operations += 1
            i += l
        else:
            i += 1
        if operations > k:
            return False
    return True


def findMaxMin(arr, n, k, l):
    low, high = min(arr), max(arr)
    while low <= high:
        mid = (low + high) // 2
        if check(arr, n, k, l, mid):
            low = mid + 1
        else:
            high = mid - 1
    return high


arr = [7, 4, 11, 2, 1, 4, 7, 5]
n = len(arr)
k = 2
l = 3
result = findMaxMin(arr, n, k, l)
print(result)
