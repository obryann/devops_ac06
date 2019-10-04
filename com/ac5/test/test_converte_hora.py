import pytest
from com.ac5.converte_hora import converteHora

"""Faz o teste de horário nulo"""


def test_hora():
    """Faz o teste com 24 horas e 60 minutos"""
    assert converteHora(24, 60) is None, 'Should be None'


"""Faz o segundo teste, teste de horário manhã"""


def test_hora2():
    """Faz o teste com 5 horas e 10 minutos"""
    assert converteHora(5, 10) == '05:10 AM'


"""Faz o terceiro teste, teste de horário da tarde"""


def test_hora3():
    """Faz o teste com 13 horas e 10 minutos"""
    assert converteHora(13, 10) == '01:10 PM'


"""faz o quarto teste, teste de horário da madrugada"""


def test_hora4():
    """Faz o teste com 0 horas e 10 minutos"""
    assert converteHora(0, 0) == '12:00 AM'
