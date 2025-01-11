# put your python code here

def C_n_k(n, k):
    if k == 0: return 1
    elif k > n: return 0
    return C_n_k(n - 1, k) + C_n_k(n - 1, k - 1)


n, k = map(int, input().split())
print(C_n_k(n, k))


