# Menu de Lanchonete (usando dicionário) :: github.com/sliatecinos
# =================================================================
# Ref.externa: https://www.facebook.com/photo?fbid=1192347487967823&set=gm.2109373895911142

# Menu de itens
dict_itens = {
    '100': ['Cachorro-quente', 9.00],
    '101': ['Cachorro-quente duplo', 11.00],
    '102': ['X-egg', 12.00],
    '103': ['X-salada', 13.00],
    '104': ['X-bacon', 14.00],
    '105': ['X-tudo', 17.00],
    '200': ['Refrigerante lata', 5.00],
    '201': ['Chá gelado', 4.00]
}

# Funcao de formatacao
def print_hs(h1, h2, h3):
    print(h1.center(6,' '), h2.ljust(32,' '), h3.rjust(5,' '),sep='|')
    pass

# Funcao de geraçao do menu de pedido
def gera_menu():
    print('='*14,'MENU:'.center(15, ' '),'='*14)
    print_hs(*['Código', 'Descrição', 'Valor'])
    print('='*45)
    for i, (codigo, dados) in enumerate(dict_itens.items()):
        print_hs(codigo, dados[0], str(dados[1]))   # chama Funcao de formataçao
    print('='*45)

# Chamada do menu de pedido
gera_menu()

pedido = []
resposta = 'S'
while resposta in 'Ss':
    codigo = input('Informe cód.pedido: ')
    if codigo not in dict_itens:
        print('OPCAO INVALIDA!!\nEscolha uma outra.')
        continue
    else:
        pedido.append(codigo)
        resposta = input('Quer pedir algo mais? S/N: ')

    if resposta not in 'Ss':
        break

# Calculo do valor total e output do pedido
valores_pedido = 0
for cod in pedido:
    for _, (k, v) in enumerate(dict_itens.items()):
        if k == cod:
            valores_pedido += v[1]

print('='*45)
print(f'\nA sua conta tem o total de: R${valores_pedido:.2f}')
