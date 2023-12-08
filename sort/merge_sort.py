def merge_sort(X):
    n = len(X)
    m = int(n/2)
    L = X[:m]
    R = X[m:]
    
    if n > 2:
        L = merge_sort(L)
        R = merge_sort(R)
    
    i = 0
    j = 0
    k = 0
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            X[k] = L[i]
            i = i+1
        else:
            X[k] = R[j]
            j = j+1
            
        k=k+1
        
    while i < len(L):
        X[k] = L[i]
        i = i+1
        k=k+1
        
    while j < len(R):
        X[k] = R[j]
        j = j+1
        k=k+1
    
    return X