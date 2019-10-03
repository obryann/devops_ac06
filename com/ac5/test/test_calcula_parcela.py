import pytest
from com.ac5.calcula_parcela import valorPagamento

def test_valorPagamento1():
	assert valorPagamento(-1, 20) == None, "Should be None"


def test_valorPagamento2():
	assert valorPagamento(80, 10) == 90.4, "Should be 90,4"


def test_valorPagamento3():
	assert valorPagamento(120, 0) == 120, "Should be 120"
