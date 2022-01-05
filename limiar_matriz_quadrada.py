# https://www.facebook.com/groups/608492105999336/permalink/2061101090738423/

# Entradas do usuario (lado, limiar, ordem da matriz)
lado_diagonal = input('Estarao "acima" ou "abaixo" da diagonal?: ')
maximo = int(input('Qual o limiar (inteiro)?: '))
ordem = int(input('Qual a ordem da matriz?: '))

# Iteraçao para popular a matriz
i = j = 0
lista_2d = []
for i in range(ordem):
    coluna = []

    for j in range(ordem):
        elemento = int(input('Elemento: '))
        coluna.append(elemento)

    lista_2d.append(coluna)


# Declaraçao da funçao que ira iterar somente sobre os itens das diagonais
def total(Matriz, Diagonal, Limiar):
    soma = 0

    for l in range(ordem):
        for m in range(ordem):
            if Diagonal == 'acima':
                if m > l:
                    soma += Matriz[l][m]

            if Diagonal == 'abaixo':
                if m < l:
                    soma += Matriz[l][m]

    return soma > Limiar


# Chamada e print do teste
teste = total(Matriz=lista_2d, Diagonal=lado_diagonal, Limiar=maximo)
print(teste)
