def max_cars_in_barge(n, L, sizes):
    M = [[[0 for _ in range(L+1)] for _ in range(L+1)] for _ in range(n+1)]

    for k in range(n, -1, -1):
        for A in range(L, -1, -1):
            for B in range(L, -1, -1):
                if k == n:
                    M[k][A][B] = 0
                else:
                    M[k][A][B] = M[k+1][A][B]  # Opção 1

                    if A >= sizes[k]:
                        M[k][A][B] = max(M[k][A][B], M[k+1][A - sizes[k]][B] + 1)  # Opção 2
                    if B >= sizes[k]:
                        M[k][A][B] = max(M[k][A][B], M[k+1][A][B - sizes[k]] + 1)

    return M[0][L][L]

# Exemplo de uso
n = 4
L = 10
sizes = [6, 3, 5, 2]
resultado = max_cars_in_barge(n, L, sizes)
print(resultado)  # Isso imprimirá o maior número de carros que podem ser colocados na balsa.
