import math

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

def is_perfect_cube(n):
    root = int(n ** (1/3))
    return root ** 3 == n

def can_break_sequence(s):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            if dp[j - 1]:
                sub = int(s[j - 1:i])
                if is_perfect_square(sub) or is_perfect_cube(sub):
                    dp[i] = True
                    break

    if not dp[n]:
        return "NÃO"

    result = []
    i = n
    while i > 0:
        for j in range(i, 0, -1):
            if dp[j - 1]:
                sub = int(s[j - 1:i])
                if is_perfect_square(sub) or is_perfect_cube(sub):
                    result.append(str(sub))
                    i = j - 1
                    break

    return "SIM\n" + " ".join(reversed(result))

# Exemplo de uso
sequence = "125271448164"
result = can_break_sequence(sequence)
print(result)
