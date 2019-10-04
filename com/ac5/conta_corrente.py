""" Módulo de contas """


class ContaCorrente:
    """ Cria classe de conta corrente """
    def __init__(self, numero, nome_correntista, saldo=0.0):
        """ Inicializa atributos da classe """

        self.numero = numero
        self.alterar_nome(nome_correntista)
        self.saldo = saldo

    def alterar_nome(self, nome_correntista):
        """ Altera o nome do titular """
        self.nome_correntista = nome_correntista

    def deposito(self, valor):
        """ Realiza depósito na conta """
        self.saldo += valor

    def saque(self, valor):
        """ Realiza saque na conta """
        self.saldo -= valor
