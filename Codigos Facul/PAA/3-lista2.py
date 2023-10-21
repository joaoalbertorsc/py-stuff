# Uma subsequˆencia cont´ıgua de uma sequˆencia S ´e uma subsequˆencia de elementos consecutivos de S.
# Por exemplo, se S = (5 15 − 30 10 − 5 40 10), ent˜ao (15 − 30 10) ´e uma subsequˆencia cont´ıgua de S, mas
# (5 15 40) n˜ao ´e. Escreva um algoritmo linear para a seguinte tarefa: receba como entrada uma sequˆencia
# de n´umeros (a1, a2, . . . , an) e devolva a subsequˆencia cont´ıgua cuja soma ´e m´axima (uma subsequˆencia de
# tamanho zero tem soma zero). No exemplo anterior, a resposta seria a subsequˆencia (10 − 5 40 10) cuja
# soma ´e 55. (Dica: Para cada j ∈ {1, 2, . . . , n}, considere subsequˆencias cont´ıguas terminando exatamente na
# posi¸c˜ao j).

def max_subarray_soma(arr):
    max_atual = max_global = arr[0]
    inicio_atual = inicio_global = fim_global = 0

    for i in range(1, len(arr)):
        if arr[i] > max_atual + arr[i]:
            max_atual = arr[i]
            inicio_atual = i
        else:
            max_atual += arr[i]

        if max_atual > max_global:
            max_global = max_atual
            inicio_global = inicio_atual
            fim_global = i

    return max_global, arr[inicio_global:fim_global+1]

# Testando o algoritmo com o exemplo fornecido
S = [5, 15, -30, 10, -5, 40, 10]
print(max_subarray_soma(S))  # Deve imprimir (55, [10, -5, 40, 10])
