import tkinter as tk
import math

def imprime(d, f, N):
    for i in range(N):
        print("Vértice", i + 1, ": Cinza =",  d[i],"; Preto =", f[i])

def loadlista():
    arquivo = open('grafo_5.txt', 'r')
    lista = arquivo.readlines()
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])
            lista_adj = [[] for _ in range(N)]
        else:
            lista_adj[int(linha[0]) - 1].append(int(linha[1]) - 1)
    arquivo.close()
    return lista_adj, N

# N = num de vertices // lista_adj = grafo

def DFS_visit(b):
    global mark
    cor[b] = "Cinza"
    mark = mark + 1
    d[b] = mark
    atualizar_cores()
    canvas.update()
    canvas.after(1000)  # Atraso de 1 segundo para visualizar a visita do vértice
    for v in lista_adj[b]:
        if cor[v] == "Branco":
            print("Aresta (", b+1, v+1,"): Árvore")
            canvas.create_line(coordenadas[b], coordenadas[v], fill='green', arrow=tk.LAST, width=3)
            DFS_visit(v)
        elif cor[v] == "Cinza":
            print("Aresta (", b+1, v+1,"): Retorno")
            canvas.create_line(coordenadas[b], coordenadas[v], fill='red', arrow=tk.LAST, width=3)
        elif d[b] < f[v]:
            print("Aresta (", b+1, v+1,"): Avanço")
            canvas.create_line(coordenadas[b], coordenadas[v], fill='blue', arrow=tk.LAST, width=3)
        else:
            print("Aresta (", b+1, v+1,"): Cruzamento")
            canvas.create_line(coordenadas[b], coordenadas[v], fill='yellow', arrow=tk.LAST, width=3)
    cor[b] = "Preto"
    mark = mark + 1
    f[b] = mark
    atualizar_cores()
    canvas.update()
    canvas.after(1000)  # Atraso de 1 segundo para visualizar o término do vértice

def DFS():
    for u in V:
        cor[u] = "Branco"

    grau_saida = [(u, len(lista_adj[u])) for u in V]
    grau_saida.sort(key=lambda x: x[1], reverse=True)
    V_ordenado = [v[0] for v in grau_saida]

    for u in V_ordenado:
        if cor[u] == "Branco":
            DFS_visit(u)
    imprime(d, f, N)  # Imprimir vetores d e f após a busca em profundidade

def atualizar_cores():
    for i in range(N):
        if cor[i] == 'Cinza':
            canvas.itemconfig(vertices[i], fill='gray')
        elif cor[i] == 'Preto':
            canvas.itemconfig(vertices[i], fill='black')

# Configuração da interface gráfica
root = tk.Tk()
root.title("Busca em Profundidade")

canvas_width = 1200
canvas_height = 800
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="dark gray")
canvas.pack()

[lista_adj, N] = loadlista()
V = list(range(0, N))
cor = ['Branco'] * N
d = [0] * N
f = [0] * N
mark = 0

vertices = []
coordenadas = []
raio = min(canvas_width, canvas_height) / 2.3
centro_x = canvas_width / 2
centro_y = canvas_height / 2

for i in range(N):
    angulo = (2 * math.pi * i) / N
    x = centro_x + int(raio * math.cos(angulo))
    y = centro_y + int(raio * math.sin(angulo))
    vertices.append(canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='white'))
    coordenadas.append((x, y))
    canvas.create_text(x, y, text=str(i+1))
    canvas.create_text(x + 30, y, text=str(i+1), anchor=tk.W)


botao = tk.Button(root, text="Iniciar Busca", command=DFS)
botao.pack()

# Janela de texto com a legenda das cores das arestas
legenda_texto = """
Legenda das Cores das Arestas:
- Verde: Aresta de Arvore
- Vermelho: Aresta de Retorno
- Azul: Aresta de Avanço
- Amarelo: Aresta de Cruzamento
"""
legenda = tk.Text(root, height=8, width=32)
legenda.insert(tk.END, legenda_texto)
legenda.pack(side=tk.LEFT)
legenda.configure(state='disabled')  # Desabilitar a edição da legenda
legenda.update_idletasks()  # Atualizar a exibição da legenda

legenda_width = legenda.winfo_width()
legenda_height = legenda.winfo_height()
legenda_x = 15
legenda_y = 15

legenda.place(x=legenda_x, y=legenda_y, anchor=tk.NW)  # Posicionar a legenda no canto esquerdo, no topo

root.configure(bg='dark gray')
root.mainloop()
