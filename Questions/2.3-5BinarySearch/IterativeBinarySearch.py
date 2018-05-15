def iterativeBinarySearch(A,q):
    low=0
    high=len(A)-1
    while low<=high:
        mid=int((low+high)/2)
        if q==A[mid]:
            return mid
        elif q>A[mid]:
            low=mid+1
        else:
            high=mid-1
    return mid
