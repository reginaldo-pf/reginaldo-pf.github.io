# BiblioTauá — Projeto Prático do Aluno (Sprint 04 - Aula 24)
## TASK-204: Motor de Validação e Aplicação de Cupons de Desconto

Bem-vindo(a) à Sprint 04 do sistema **BiblioTauá Livraria Web**!

Este repositório contém a base pré-existente (v0.3.0) da livraria universitária (`Cliente`, `Livro`, `ItemPedido`, `Pedido`, banco SQLite) e o esqueleto inicial das tarefas que você implementará na **Aula 24**.

---

## 🎯 Suas Tarefas Hoje

1. **`bibliotaua/exceptions.py`:**
   - Implementar as subclasses de exceção que herdam de `CupomInvalidoError` *(Slide 12)*:
     - `CupomInexistenteError`
     - `CupomInativoError`
     - `CupomExpiradoError`
     - `CupomEsgotadoError`
     - `ValorMinimoNaoAtingidoError`

2. **`bibliotaua/models/cupom.py`:**
   - Implementar validações no método `__post_init__` *(Slide 13 e Guia do Desenvolvedor Passo 2.3)*.
   - Implementar os métodos de domínio *(Slides 14 e 15 e Guia do Desenvolvedor Passos 2.4 a 2.9)*:
     - `obter_data_validade()`
     - `esta_expirado(data_referencia)`
     - `atingiu_limite_usos()`
     - `registrar_uso()`
     - `pode_ser_aplicado_ao_pedido(subtotal, data_referencia)`
     - `calcular_desconto(subtotal, data_referencia)`

3. **`main.py`:**
   - Criar ou completar o arquivo `main.py` na raiz do projeto para instanciar o cupom e testar o cálculo de desconto e o bloqueio de valor mínimo *(Slide 16 e Guia do Desenvolvedor Passo 3)*.

---

## 🚀 Como Executar

No terminal, execute:

```bash
python3 main.py
```

**Saída esperada:**

```text
--- Testando a Entidade Cupom (BiblioTauá) ---
Cupom: BEMVINDO10 (10.0% OFF)
Subtotal R$ 100.00 -> Desconto: R$ 10.00
Subtotal R$ 30.00  -> Bloqueado: O cupom 'BEMVINDO10' exige pedido mínimo de R$ 50.00. Subtotal atual: R$ 30.00.
```
