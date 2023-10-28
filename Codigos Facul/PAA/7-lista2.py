import heapq
from collections import defaultdict

# Função para construir a árvore de Huffman
def construir_arvore_huffman(frequencias):
    fila = [[peso, [simbolo, ""]] for simbolo, peso in frequencias.items()]
    heapq.heapify(fila)

    while len(fila) > 1:
        menor = heapq.heappop(fila)
        segundo_menor = heapq.heappop(fila)
        for par in menor[1:]:
            par[1] = '0' + par[1]
        for par in segundo_menor[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(fila, [menor[0] + segundo_menor[0]] + menor[1:] + segundo_menor[1:])

    return sorted(fila[0][1:], key=lambda p: (len(p[-1]), p))

# Função para calcular o tamanho do texto codificado usando a árvore de Huffman
def tamanho_texto_codificado(texto, arvore_huffman):
    codificacao = dict(arvore_huffman)
    tamanho = 0
    for simbolo in texto:
        tamanho += len(codificacao[simbolo])
    return tamanho

# Exemplo de texto e frequências
texto = "ABCDABEEFGABCDEFAACCDABCG"
frequencias = defaultdict(int)
total_caracteres = len(texto)

for simbolo in texto:
    frequencias[simbolo] += 1

# Algoritmo para obter um código de Huffman ternário
arvore_huffman_ternario = construir_arvore_huffman(frequencias)

# Algoritmo para obter um código de Huffman ao-contrário (pior código livre de prefixo possível)
arvore_huffman_ao_contrario = construir_arvore_huffman(frequencias[::-1])

# Codificação de tamanho fixo (3 bits por símbolo)
tamanho_codificacao_fixa = total_caracteres * 3

# Tamanho do texto codificado usando os algoritmos
tamanho_huffman_ternario = tamanho_texto_codificado(texto, arvore_huffman_ternario)
tamanho_huffman_ao_contrario = tamanho_texto_codificado(texto, arvore_huffman_ao_contrario)

# Resultados
print(f"Tamanho do texto codificado com Huffman Ternário: {tamanho_huffman_ternario} bits")
print(f"Tamanho do texto codificado com Huffman ao-contrário: {tamanho_huffman_ao_contrario} bits")
print(f"Tamanho do texto codificado com Codificação de Tamanho Fixo: {tamanho_codificacao_fixa} bits")
