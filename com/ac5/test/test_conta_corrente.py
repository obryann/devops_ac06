import pytest
from com.ac5.conta_corrente import ContaCorrente

conta_corrente = ContaCorrente(1, "Mateo Pallini", 0.0)


def test_alterarNome():
    conta_corrente.alterar_nome("Mateo Pallini")
    assert conta_corrente.nome_correntista == "Mateo Pallini"


def test_deposito():
    conta_corrente.deposito(150)
    assert conta_corrente.saldo == 150
    conta_corrente.deposito(50)
    assert conta_corrente.saldo == 200


def test_saque():
    conta_corrente.saque(199)
    assert conta_corrente.saldo == 1
