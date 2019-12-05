def mat_exp(A,N):
    res = [[1,0],[0,1]] # identity matrix
    while N > 0:
        if N % 2:
            res = matrix_mult(res,A)
        A = matrix_mult(A,A)
        N //= 2
    return res

def matrix_mult(A,B,mod=10**9+7):
    """both 2 dim matrices"""
    C = [[1,1],[1,1]]
    C[0][0] = ((A[0][0]*B[0][0])%mod + (A[0][1]*B[1][0])%mod)%mod
    C[0][1] = ((A[0][0]*B[0][1])%mod + (A[0][1]*B[1][1])%mod)%mod
    C[1][0] = ((A[1][0]*B[0][0])%mod + (A[1][1]*B[1][0])%mod)%mod
    C[1][1] = ((A[1][0]*B[0][1])%mod + (A[1][1]*B[1][1])%mod)%mod
    return C

def fib(N):
    m_fib = [[1,1],[1,0]]
    exp = mat_exp(m_fib,N)
    return exp

n = int(input())
arr = fib(n)
print(arr[0][0],arr[0][1],arr[1][1], sep='\n')
