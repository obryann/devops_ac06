"""Função"""


def converteHora(hora24, minuto24):
    """Verifica se os valores são válidos"""
    if (hora24 > 23) or (hora24 < 0) or (minuto24 < 0) or (minuto24 > 59):
        return None
    """Verifica se a hora é igual a zero"""
    if (hora24 < 12):
        if (hora24 == 0):
            hora24 = 12
        return '%02d:%02d AM' % (hora24, minuto24)
    """Verifica se a hora é maior que 12"""
    if (hora24 > 12):
        hora24 -= 12
    return '%02d:%02d PM' % (hora24, minuto24)
