def merge(a, b):
    res = []
    ca = 0
    cb = 0

    while ca < len(a) and cb < len(b):
        if a[ca] < b[cb]:
            res.append(a[ca])
            ca += 1
        else:
            res.append(b[cb])
            cb += 1

    if ca == len(a):
        while cb < len(b):
            res.append(b[cb])
            cb += 1
    else:
        while ca < len(a):
            res.append(a[ca])
            ca += 1

    return res

def mergesort(array, n):
    if n <= 1:
        return array

    midpoint = int(n/2)

    if n & 1:
        l1 = mergesort(array[:midpoint], n//2)
        l2 = mergesort(array[midpoint:], n//2+1)
    else:
        l1 = mergesort(array[:midpoint], n//2)
        l2 = mergesort(array[midpoint:], n//2)
    return merge(l1, l2)


def inversions(low, high, array):
    if high == low:
        return 0

    mid = int((high + low) / 2) + 1

    numInversions = inversions(low, mid-1, array) + inversions(mid, high, array)
    i = low

    for j in array[mid:high+1]:
        while i <= mid-1 and array[i] <= j:
            i += 1

        numInversions += (mid - i)
        if i > mid-1:
            break

    spliceIn = array[low:high+1].copy()
    spliceIn = mergesort(spliceIn, len(spliceIn))

    array[low:high+1] = spliceIn

    return numInversions


size = int(input())
arr = [int(x) for x in input().split(" ")]

print(inversions(0,size-1,arr))
