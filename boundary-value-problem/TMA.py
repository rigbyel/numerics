def tridiag_matrix_algorithm(a, b, c, d):
    n = len(d)
    a.insert(0,0)
    c.append(0)
    c[0] /= b[0]
    d[0] /= b[0]

    for i in range(1, n):
        c[i] /= b[i] - a[i]*c[i-1]
        d[i] = (d[i] - a[i]*d[i-1]) / (b[i] - a[i]*c[i-1])

    for i in range(n-2, -1, -1):
        d[i] -= c[i]*d[i+1]
    
    return d


def tma(A, B, C, D):
    n = len(B)
    a = [0]*n
    b = [0]*n

    a[0] = -C[0]/B[0]
    b[0] = D[0]/B[0]

    # первый этап прогонки
    for i in range(1, n-1):
        a[i] = - C[i] / (A[i]*a[i-1] + B[i])
        b[i] = (D[i] - A[i]*b[i-1]) / (A[i]*a[i-1] + B[i])
    
    u = [0]*n
    u[-1] =(D[-1] - A[-1]*b[-2]) / (A[-1]*a[-2] + B[-1])

    # второй этап прогонки
    for i in range(n-2, -1, -1):
        u[i] = a[i]*u[i+1] + b[i]

    return u
