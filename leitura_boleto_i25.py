# Leitura de Boleto I25 (BR) :: github.com/sliatecinos
# Refs.: https://stackoverflow.com/questions/59617527/pyzbar-not-detecting-code93-barcodes
# https://stackoverflow.com/questions/72267024/why-does-pyzbar-remove-some-digits-from-the-barcode?fbclid=IwAR15ekypJiaXhJ-sgkmxGAIgS743HP6DA2si0LnA4OTijvxx3hj7YCXYICE
# ====================================================
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from textwrap import wrap
import cv2


def ult_dig(quadrantes):
    """
    Funçao para calculo do DV do quadrante do codigo
    """
    novos_quadrantes = []
    for quadrante in quadrantes:
        validadores = list(range(2,10))
        validadores.extend([2,3,4])
        digitos = list(map(int, list(quadrante[::-1])))
        modulo = sum([a * b for a, b in zip(validadores, digitos)]) % 11
        dv = 0 if modulo in [0,1] else 11 - modulo
        novos_quadrantes.append(quadrante+str(dv))
    return novos_quadrantes

def decode_codigo(codigo):
    im = cv2.imread(codigo, cv2.IMREAD_GRAYSCALE)
    _, bw_im = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
    cod_decoded = decode(bw_im, symbols=[ZBarSymbol.I25])
    return wrap(cod_decoded[0][0].decode('UTF-8'), 11)   # wrap usado pra dividir a string em "partes-n"


cd_barras = 'boleto_claro.png'
codigo_decoded = decode_codigo(cd_barras)
print('.'.join(ult_dig(codigo_decoded)))

## Outputs: "858200000260.178601801205.529544183860.673925100017"
