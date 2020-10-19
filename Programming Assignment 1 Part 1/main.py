# Cole Schutzman                                                                     cms7721
# Tanner Mahofski                                                                    tzm5490
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

def msort(a, n):
    if n <= 1:
        return a

    midpoint = n//2

    if n & 1:
        l1 = msort(a[:midpoint], n//2)
        l2 = msort(a[midpoint:], n//2+1)
    else:
        l1 = msort(a[:midpoint], n//2)
        l2 = msort(a[midpoint:], n//2)
    return merge(l1, l2)


length = int(input())
arr = [int(i) for i in input().split()]
res = msort(arr, length)

for i in res:
    print(i, end=" ")