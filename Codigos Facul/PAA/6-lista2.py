import scanf as scanf


def existe_subconjunto_com_soma(T, lista):
    n = len(lista)
    dp = [[False for _ in range(T + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for s in range(1, T + 1):
        dp[0][s] = False

    for i in range(1, n + 1):
        for s in range(1, T + 1):
            if lista[i - 1] > s:
                dp[i][s] = dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s] or dp[i - 1][s - lista[i - 1]]

    return dp[n][T]


# Exemplo de uso
T = int(input("digite o seu número: "))
lista = [7, 21, 1, 87, 3, 12]

if existe_subconjunto_com_soma(T, lista):
    print("Sim, existe um subconjunto com soma igual a", T)
else:
    print("Não, não existe um subconjunto com soma igual a", T)
