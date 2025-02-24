import sys

# input handling and generate xT
degree = int(sys.stdin.readline().strip())
N1 = list(map(int, sys.stdin.readline().strip().split()))
N = [1] + list(map(int, sys.stdin.readline().strip().split()))
Q = int(sys.stdin.readline().strip())
tms = []
for i in range(Q):
    T, M = sys.stdin.readline().strip().split()
    tup = (int(T), int(M))
    tms.append(tup)
coeff = [N1[0]] + N1[-1:0:-1]
xT = [[k] for k in N]


# define matrix multiplication
def mult(A, B, mod):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])

    if cols_a != rows_b:
        return

    # Create the result matrix with dimensions rows_a x cols_b
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for k in range(cols_a):
            if A[i][k] != 0:
                for j in range(cols_b):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

# define exponentiation
def matrix_expo(base, exp, mod):
    if exp == 1:
        return base
    if exp % 2 == 0:
        half_power = matrix_expo(base, exp // 2, mod)
        return mult(half_power, half_power, mod)
    return mult(base, matrix_expo(base, exp - 1, mod), mod)

# Make matrix
mat = [ [1] + [0] * degree ]
for i in range(1, degree):
  row = [0]*(i+1)
  row.append(1)
  mat.append(row + [0] * (degree-i-1))
mat.append(coeff)

for tm in tms:
  T = tm[0]
  M = tm[1]
  new_m = matrix_expo(mat,T,M)
  new_coeff = mult(new_m, xT, M)
  print(new_coeff[1][0])
