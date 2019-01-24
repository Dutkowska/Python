def heaps(A, n):
    if n==1:
        print(*A, sep="-")
    else:
        for i in range(n-1):
            heaps(A, n-1)
            j = 0 if (n%2)==1 else i
            A[j], A[n-1]=A[n-1], A[j]
        heaps(A, n-1)
B=[1,2,3]
heaps(B, len(B))