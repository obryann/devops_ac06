""" Testa módulo de Conta Corrente """
from com.ac5.conta_corrente import ContaCorrente

CONTA_CORRENTE = ContaCorrente(1, "Mateo Pallini", 0.0)


def test_alterar_nome():
    """ Testa função de alterar nome """
    CONTA_CORRENTE.alterar_nome("Mateo Pallini")
    assert CONTA_CORRENTE.nome_correntista == "Mateo Pallini"


def test_deposito():
    """ Testa função de depósito """
    CONTA_CORRENTE.deposito(150)
    assert CONTA_CORRENTE.saldo == 150
    CONTA_CORRENTE.deposito(50)
    assert CONTA_CORRENTE.saldo == 200


def test_saque():
    """ Testa função de saque """
    CONTA_CORRENTE.saque(199)
    assert CONTA_CORRENTE.saldo == 1
