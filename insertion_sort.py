def insertion_sort(X):
    for i in range(len(X)):
        key = X[i]
        j = i-1
        while (j >= 0) and (X[j] > key):
            X[j+1] = X[j]
            j = j-1
        
        X[j+1] = key
    return