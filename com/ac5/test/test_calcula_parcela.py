from com.ac5.calcula_parcela import valor_pagamento

"""teste de valor de pagamento"""


def test_valor_pagamento1():
    """verifica se é vazio"""
    assert valor_pagamento(-1, 20) == 0, "Should be 0"


"""teste de valor de pagamento"""


def test_valor_pagamento2():
    """ verifica se é 90.4"""
    assert valor_pagamento(80, 10) == 90.4, "Should be 90,4"


"""teste de valor de pagamento"""


def test_valor_pagamento3():
    """ verifica se é 120"""
    assert valor_pagamento(120, 0) == 120, "Should be 120"