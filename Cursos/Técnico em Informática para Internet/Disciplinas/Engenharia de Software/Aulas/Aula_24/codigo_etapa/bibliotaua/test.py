from bibliotaua.models.cupom import Cupom, TipoDesconto
from datetime import date, timedelta
cupom = Cupom(
    codigo = "BEMVINDO10",
    tipo_desconto = TipoDesconto.PERCENTUAL,
    valor_desconto = 10.0,
    valor_minimo_pedido = 50.0,
    validade_ate = date.today() + timedelta(days = 5)
)
# Teste 1: Subtotal R$ 100.00 ( valido )
cupom.calcular_desconto(100.0)
# Teste 2: Subtotal R$ 30.00 ( abaixo do minimo )
cupom.calcular_desconto(30.0)
