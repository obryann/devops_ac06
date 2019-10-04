import pytest 
from com.ac5.converte_hora import converteHora


def test_hora():
    assert converteHora(24, 60) is None, 'Should be None'


def test_hora2():
    assert converteHora(5, 10) == '05:10 AM'


def test_hora3():
    assert converteHora(13, 10) == '01:10 PM'


def test_hora4():
    assert converteHora(0, 0) == '12:00 AM'
