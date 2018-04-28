def Merge(A,p,q,r):
    L=A[p:q]
    R=A[q:r]
    i=0
    j=0
    for k in range(p,r):
        if i>=len(L):
            A[k] = R[j]
            j+=1
        elif j>=len(R):
            A[k] = L[i]
            i+=1
        elif L[i]<=R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
def MergeSort(A,p,r):
    if p<r-1:
        q = int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q,r)
        Merge(A,p,q,r)
