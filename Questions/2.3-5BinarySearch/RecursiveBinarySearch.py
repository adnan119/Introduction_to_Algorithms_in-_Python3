def recursiveBinarySearch(A,q,low,high):
    mid=int((low+high)/2)
    if low>high:
        return None
    elif A[mid]<q:
        return recursiveBinarySearch(A,q,mid+1,high)
    elif A[mid]>q:
        return recursiveBinarySearch(A,q,low,mid-1)
    else:
        return mid
