import pytest
from com.ac5.converte_hora import converte_hora


def test_hora():
    assert converte_hora(24, 60) is None, 'Should be None'


def test_hora2():
    assert converte_hora(5, 10) == '05:10 AM'


def test_hora3():
    assert converte_hora(13, 10) == '01:10 PM'


def test_hora4():
    assert converte_hora(0, 0) == '12:00 AM'
