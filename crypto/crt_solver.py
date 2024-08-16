from math import gcd

# Function to compute the extended GCD of a and b
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Function to solve the system of congruences for two moduli
def system_solver(a, b, s, t):
    _, alpha, beta = xgcd(s, t)
    x = (alpha * b * s + beta * a * t) % (s * t)
    return x, s * t

# CRT solver definition, L is the list of remainders and M is the list of pairwise coprime moduli
def crt_solver(L, M):
    # Test that L and M have the same size
    if len(L) != len(M):
        return "Error: the lists have not the same length"

    m = len(L)

    if m == 1:
        return L[0] % M[0]

    # Test that each element of L is >= 0 and is an integer
    for integer in L:
        if integer < 0 or not isinstance(integer, int):
            return "Error: list L must contain integers greater or equal than zero"

    # Test that each element of M is > 0 and is an integer
    for integer in M:
        if integer <= 0 or not isinstance(integer, int):
            return "Error: list M must contain integers greater than zero"

    # Test that elements of M are pairwise coprime
    for i in range(m - 1):
        for j in range(i + 1, m):
            if gcd(M[i], M[j]) != 1:
                return "Error: modules are not pairwise coprime"

    # Solving the first two equations of the system
    x, n = system_solver(L[0], L[1], M[0], M[1])

    # Solving the whole system
    for i in range(2, m):
        x, n = system_solver(x, L[i], n, M[i])

    return x

# Example usage
L=[2,3,1]
M=[3,4,5]
result = crt_solver(L, M)
print(result)  # Output should be the solution to the system of congruences
