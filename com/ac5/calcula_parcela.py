""" Função """


def valor_pagamento(valor, dias_atraso):
    """ verifica o valor de pagamento conforme os dias de atraso """
    if valor < 0:
        return 0
    if dias_atraso > 0:
        multa = valor * 0.03
        adicional_atraso = valor * (dias_atraso * 0.01)
        return valor + multa + adicional_atraso
    if dias_atraso <= 0:
        return valor