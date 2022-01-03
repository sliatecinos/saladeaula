# https://www.facebook.com/groups/pypcom/permalink/1668364116833984/
tijolo_curto = '[ ]'
tijolo_longo = '[    ]'

l = int(input('Informe largura: '))
h = int(input('Informe altura: '))


for i in range(h):
    if i % 2 == 0:
        # Inicio bloco preenche linha par
        print(tijolo_longo * (l // 2), end='')
        if l % 2 > 0:
            print(tijolo_curto, end='')
        print()
    else:
        # Inicio bloco preenche linha impar
        print(tijolo_curto + tijolo_longo * ((l // 2)-1), end='')
        if l % 2 > 0:
            print(tijolo_longo, end='')
        else:
            print(tijolo_curto, end='')
        print()
        