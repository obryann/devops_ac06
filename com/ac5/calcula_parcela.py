""" Função """


def valor_pagamento(valor, diasAtraso):
    """ verifica o valor de pagamento conforme os dias de atraso """
    if (valor < 0):
        return None
    if (diasAtraso > 0):
        multa = valor * 0.03
        adicionalAtraso = valor * (diasAtraso * 0.01)
        return valor + multa + adicionalAtraso
    else:
        return valor
