def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [n1]
    R = [n2]

    for i in range(n1):
        L[i] = A[p+i-1]
    for j in range(n2):
        R[j] = A[q+j]

    i = j = k = 0

    # to do......




