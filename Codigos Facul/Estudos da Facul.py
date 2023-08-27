print("Exercicio 1:", "impossivel")
print()


'#exercicio 2'
'#Apenas Resolução de problemas'
import math

print("Exercicio 2:")
A = 5
B = 10
C = -8
D = 1.5

X = 2 * A % 3 - C
print("A =", X)

X1 = math.sqrt(-2 * C) / 4
print("B =", X1)

X2 = ((20 / 3) / 3) + 8 ** 2 / 2
print("C =", X2)

X3 = 5 * 3 + 15 % 5 + 8 - 1 * 20 / 15
print("D =", X3)

X4 = math.sqrt(A ** (A / B)) + C * D
print("E =", X4)

X5 = 5 ** 2 - math.sqrt(125) * 0 / 540 - 10 / 2
print("F =", X5)
print()

print("Exercicio 3")
Xda3 = -1
Yda3 = 3
Zda3 = 7
print('Não faço ideia.')
print()


'#exercicio 4'
'#Apenas Resolução de problemas'
print("Exercicio 4:")

A = 2
B = 7
C = 3.5
L = False

Y = B == A * C and L or True
if Y == L:
    print("A = false")
else:
    print("A = true")

Y1 = B > A or B == A ** A
if Y1 == L:
    print("B = false")
else:
    print("B = true")

Y2 = L and B / A >= C or not A <= C
if Y2 == L:
    print("C = false")
else:
    print("C = true")

Y3 = not L or True and math.sqrt(A + B) >= C
if Y3 == L:
    print("D = false")
else:
    print("D = true")

Y4 = L or B ** A <= C * 10 + A * B
if Y4 == L:
    print("E = false")
else:
    print("E = true")
print()


'#exercicio 5'
print("exercicio 5:")

Dolar = 'Dolar'
Real = 'Real'
moeda = input('Escreva "Real" ou "Dolar" e converta a moeda escolhida:')
print('Conversão do', moeda, ':')
if moeda == Dolar:
    cotacao1 = float(input('Cotação atual do Real para a moeda desejada?'))
    montante1 = float(input('Quantos reais deseja converter?'))
    dolar = cotacao1 * montante1
    print('A quantidade de reais em dolares são de U$', dolar)
if moeda == Real:
    cotacao = float(input('Cotação atual do Dolar para a moeda desejada?'))
    montante = float(input('Quantos dolares deseja converter?'))
    real = cotacao * montante
    print('A quantidade de dolares em reais são de R$', real)
print()


'#exercicio 6'
print("exercicio 6:")
Numero_Inteiro = 6

print("Resposta:", Numero_Inteiro - 1, ",", Numero_Inteiro + 1)
print()


'#exercicio 7'
print("Exercicio 7")
B = 2
h = 4
Area_do_retangulo = ((B * h) * 2)

print("Area do Retangulo =", Area_do_retangulo)
print()


"#Exercicio 8"
'#Z variável X do exemplo'
print("Exercicio 8")
Z = 6
Z_resultado = (3 * (Z ** 2) - 6 * Z + 5)

print("Resultado da Função =", Z_resultado)
print()


'#Exercicio 9'
print("Exercicio 9:")
# Ada9 = 2
# Bda9 = 3
# Cda9 = 4
# Xda9 = 1
# if ((Ada9 * Xda9) ^ 2 + Bda9 * Xda9 + Cda9 = 0):
#     print(Ada9, Bda9, Cda9)
# else:
print('F total')
print()


print('Exercicio 10:')
Xda10 = 1
Ada10 = 2
Bda10 = 3
Cda10 = 4
Yda10 = (Ada10 * Xda10) ** 2 + Bda10 * Xda10 + Cda10

print('Y =', Yda10)
print('A, B, C =', Ada10, Bda10, Cda10)
print()


print('Exercicio 11:')
print('Ez bugs')
print()


print('Exercicio 12:')
print('F total 2.0')
print()

######################################################################
'#imput = dado do usuario'
nome = input('qual o seu nome?')
idade = input("qual a sua idade?")
print(f'nome do usuário é', nome, 'e a idade do usuário é de', idade)
