import pytest
from com.ac5.calcula_parcela import valorPagamento


def test_valor_pagamento1():
    assert valor_pagamento(-1, 20) is None, "Should be None"


def test_valor_pagamento2():
    assert valor_pagamento(80, 10) == 90.4, "Should be 90,4"


def test_valor_pagamento3():
    assert valor_pagamento(120, 0) == 120, "Should be 120"
