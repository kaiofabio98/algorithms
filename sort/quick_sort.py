def quick_sort(A, first, last):
    if first < last:
        split_point = partition(A, first, last)
        quick_sort(A, first, split_point-1)
        quick_sort(A, split_point+1, last)
    
def partition(A, first, last):
    pivo = A[first]
    L = first+1
    R = last
    done = False
    
    while not done:
        while L <= R and A[L] <= pivo:
            L = L+1
        while A[R] >= pivo and R >= L:
            R = R-1
            
        if R<L:
            done = True
        else:
            aux = A[L]
            A[L] = A[R]
            A[R] = aux
            
    aux = A[first]
    A[first] = A[R]
    A[R] = aux
    
    return R