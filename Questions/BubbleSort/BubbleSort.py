def BubbleSort(A):
    for i in range(len(A)):
        for j in range(A.index(A[-1]),i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
