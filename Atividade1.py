# ============================================
# ATIVIDADE DE PYTHON
# ============================================


# ============================================
# 1) Lista com cinco números inteiros
# ============================================

# Criando uma lista vazia
numeros = []

# Pedindo 5 números ao usuário
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)  # adiciona o número na lista

# Exibindo os elementos da lista
print("\nElementos da lista:", numeros)

# Calculando a soma dos valores da lista
soma = sum(numeros)

# Mostrando o resultado
print("Soma dos valores:", soma)


# ============================================
# 2) Função recursiva para somar de 1 até n
# ============================================

def soma_recursiva(n):
    # Caso base da recursão
    if n == 1:
        return 1
    # Chamada recursiva
    else:
        return n + soma_recursiva(n - 1)

# Pedindo um número ao usuário
numero = int(input("\nDigite um número inteiro positivo: "))

# Mostrando o resultado da soma
print("Soma de 1 até", numero, "=", soma_recursiva(numero))


# ============================================
# 3) Trabalhando com vetor (lista)
# ============================================

vetor = [10, 20, 30, 40, 50]

# Acessando posições do vetor
print("\nValor de vetor[0]:", vetor[0])
print("Valor de vetor[3]:", vetor[3])

# Explicação:
# Em Python, os índices começam em 0.
# Ou seja, o primeiro elemento da lista está na posição 0.


# ============================================
# 4) Trabalhando com matriz
# ============================================

matriz = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

# Acessando elementos da matriz
print("\nValor de matriz[0][2]:", matriz[0][2])
print("Valor de matriz[2][1]:", matriz[2][1])

# Explicação:
# O primeiro índice representa a linha
# O segundo índice representa a coluna


# ============================================
# 5) Identificando tipos de dados
# ============================================

x = 15
y = 3.5
z = "Python"
w = False

print("\nTipos das variáveis:")
print("x:", type(x))
print("y:", type(y))
print("z:", type(z))
print("w:", type(w))


# ============================================
# 6) Programa para calcular média de notas
# ============================================

notas = []

# Recebendo três notas
for i in range(3):
    nota = float(input("\nDigite uma nota: "))
    notas.append(nota)

# Calculando média
media = sum(notas) / 3

print("Média das notas:", media)


# ============================================
# 7) Criando um dicionário de aluno
# ============================================

aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Informática",
    "media_final": media
}

# Exibindo apenas nome e média
print("\nInformações do aluno:")
print("Nome:", aluno["nome"])
print("Média Final:", aluno["media_fina
