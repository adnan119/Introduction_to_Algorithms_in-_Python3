def countInversionNMergeSort(A,p,q,r):
    L=A[p:q]
    R=A[q:r]
    i=0
    j=0
    inversions=0
    for k in range(p,r):
        if i>=len(L):
            A[k] = R[j]
            j+=1
        elif j>=len(R):
            A[k] = L[i]
            i+=1
        elif L[i]<R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
            inversions+=len(L)-i
    return inversions
def countInversionNSort(A,p,r):
    if p>=r-1:
        return 0
    q=int((p+r)/2)
    inversions=countInversionNSort(A,p,q)
    inversions+=countInversionNSort(A,q,r)
    inversions+=countInversionNMergeSort(A,p,q,r)
    return inversions

