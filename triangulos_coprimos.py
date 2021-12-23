# _*_ coding: utf-8 _*_
# Gere os 100 primeiros triangulos de pitagoras que os catetos e hipotenusa
# sao coprimos entre si (MDC==1)
# Ref. externa: https://pt.quora.com/O-que-s%C3%A3o-os-tri%C3%A2ngulos-pitag%C3%B3ricos-e-como-calcul%C3%A1-los

# Definicao de MDC (terno de co-Primos):
def mdc(a, b, c):
    #     a = 45,#     b = 90,#     c = 120
    mdc = c
    while c % mdc != 0 or b % mdc != 0 or a % mdc != 0:
        mdc = mdc - 1
    return mdc
# print('MDC(', a, ',', b, ',', c, '): ', mdc(45,90,120))


# Definicao de triangulo retangulo (a2 + b2 = c2):
def eh_retangulo(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False
# print('Eh retangulo (', a, ',', b, ',', c, '): ', eh_retangulo(3, 4, 5))

# Brute-force pra encontrar os 100 triangulos:
# ============================================
x=1
y=0
d=1
teto=100
contador=0
triangulos_ABC=[]

while True:
    if contador == teto:
        break
    else:
        y = 0

    while y < x:
        if contador == teto:
            break
        else:
            d = 0

        while d <= x:
            if contador == teto:
                break

            A = (x ** 2 - y ** 2) * d   # Encontre a): a=(x2–y2)⋅d
            B = 2 * x * y * d           # Encontre b): b=2xy⋅d
            C = (x ** 2 + y ** 2) * d   # Encontre c): c=(x2+y2)⋅d (x..4, y..1, d..1)
            if (A > 0 and B > 0 and C > 0) and (A < C) and (B < C):   # (D_C)Elimina resultados negativos
                # valida se o terno sao "coprimos" entre si (MDC=1) e se eh pitagorico
                if mdc(A, B, C) == 1 and eh_retangulo(A, B, C):
                    sorted_numeros = tuple(sorted((A, B, C)))   # Classif A,B,C
                    triangulos_ABC.append(sorted_numeros)
                    contador = contador + 1   # +1 triangulo encontrado

            d = d + 1
        y = y + 1
    x = x + 1

# Ref. externa: https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
def Sort(sub_li):
    '''Funcao aux de ordenacao das tuplas por cada A'''
    return sorted(sub_li, key=lambda x: x[0])


print(f'Os primeiros {len(triangulos_ABC)} triangulos pitagoricos e coprimos entre si, sao:\n{Sort(triangulos_ABC)}')
