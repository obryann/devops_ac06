""" Módulo de testes """
from com.ac5.converte_hora import converte_hora


def test_hora():
    """ Testa com hora 1 """
    assert converte_hora(24, 60) is None, 'Should be None'


def test_hora2():
    """ Testa com hora 2 """
    assert converte_hora(5, 10) == '05:10 AM'


def test_hora3():
    """ Testa com hora 3 """
    assert converte_hora(13, 10) == '01:10 PM'


def test_hora4():
    """ Testa com hora 4 """
    assert converte_hora(0, 0) == '12:00 AM'
