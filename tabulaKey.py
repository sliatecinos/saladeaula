# _*_ coding: utf-8 _*_
# ================================================================================================
# Tabula Key :: github.com/sliatecinos
# Ref.externa: https://www.facebook.com/photo.php?fbid=303631988335745&set=p.303631988335745&type=3
# ================================================================================================

def tabulaKey():
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tabela = []
    itens = range(len(letras))
    for i in itens:
        chave = letras[i:] + letras[:i]
        tabela.append(chave)

    return tabela


print(tabulaKey()[0])
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(tabulaKey()[12])
# MNOPQRSTUVWXYZABCDEFGHIJKL
print(tabulaKey()[25])
# ZABCDEFGHIJKLMNOPQRSTUVWXY
