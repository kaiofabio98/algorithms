def bubble_sort(X):
    for last in range(len(X)-1,0,-1):
        for i in range(last):
            if X[i] > X[i+1]:
                aux = X[i]
                X[i] = X[i+1]
                X[i+1] = aux
                
    return X