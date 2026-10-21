# Guia Pedagógico: Projeto Final por Fases / Aulas
## Sistema de Planejamento Financeiro Pessoal com Previsão de Renda e Gastos

* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) – Campus Tauá
* **Curso:** Técnico em Redes de Computadores / Integrado e Subsequente
* **Disciplina:** Lógica de Programação com Python
* **Carga Horária Total Prevista:** 10 horas-aula (5 encontros de 2 h/a cada — 90 a 100 min por aula)
* **Metodologia:** *Live Coding Dialogado*, *Desenvolvimento Incremental (Baby Steps)* e *Aprendizagem Baseada em Projetos (PBL)*.

---

## 📌 Visão Geral da Abordagem por Fases

A principal barreira dos estudantes de nível técnico ao desenvolver seu primeiro projeto é o **bloqueio diante da folha em branco** e a sobrecarga cognitiva ao tentar implementar regras de negócio, interface e persistência simultaneamente.

Por essa razão, o projeto foi fatiado em **5 fases incrementais**. Em cada aula os alunos constroem uma fatia funcional do software. Ao soar o sinal de cada encontro, **o código sempre executa sem quebrar**, oferecendo um sentimento palpável de evolução e autoria.

```
       [Aula 1] Menu & Fluxo Principal (Loop while, if/elif/else, Stubs)
                           │
                           ▼
       [Aula 2] Validação Segura & Previsão de Renda (try/except, return)
                           │
                           ▼
       [Aula 3] Cadastro de Despesas (Dicionários, Listas e append)
                           │
                           ▼
       [Aula 4] Visualização Tabular (Laço for, enumerate, f-strings alinhadas)
                           │
                           ▼
       [Aula 5] Inteligência de Negócio & Relatório 50-30-20 (Acumuladores & Diagnóstico)
```

---

## 🗺️ Mapa de Competências e Cronograma Resumido

| Encontro | Fase / Tema | Conceitos Principais de Programação | Entrega Funcional da Aula | Arquivo de Apoio |
| :---: | :--- | :--- | :--- | :--- |
| **Aula 1** | **A Arquitetura e o Menu Interativo** | Funções sem parâmetro/retorno, `while True`, `break`, `input()`, `if/elif/else`. | Menu que reage às opções, não morre na primeira escolha e aceita sair limpo (opção 0). | [etapa1_menu_e_fluxo.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa1_menu_e_fluxo.py) |
| **Aula 2** | **Entrada Segura & Previsão de Renda** | Funções com parâmetro e `return`, `try/except ValueError`, `float`, formatação monetária. | Opção 1 funcional: usuário define renda com blindagem contra letras e números negativos. | [etapa2_validacao_e_renda.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa2_validacao_e_renda.py) |
| **Aula 3** | **Modelando Entidades: Despesas** | Dicionários (`dict`), listas dinâmicas (`list`), `.append()`, manipulação de strings (`.strip()`). | Opção 2 funcional: cadastro de despesas com descrição, valor e submenu de categoria. | [etapa3_cadastro_despesas.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa3_cadastro_despesas.py) |
| **Aula 4** | **Visualização Formatada em Tabela** | Laço `for in`, `enumerate()`, formatação alinhada (`<`, `>`), cláusula de guarda. | Opção 3 funcional: listagem formatada em colunas alinhadas no terminal. | [etapa4_listagem_despesas.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa4_listagem_despesas.py) |
| **Aula 5** | **Relatório Analítico & Regra 50-30-20** | Acumuladores condicionais, cálculos percentuais, diagnósticos orçamentários, `__name__`. | Sistema 100% integrado com análise de superávit/déficit e recomendação 50-30-20. | [etapa5_projeto_completo.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa5_projeto_completo.py) |

---

## 📖 Roteiro Detalhado de Execução por Aula

---

### 🔹 AULA 1: A Arquitetura do Sistema e o Loop Principal
* **Duração:** 90 minutos
* **Objetivo Geral:** Construir a espinha dorsal de um software CLI interativo e desmistificar a arquitetura de eventos orientada a menu.

#### 1. Contextualização e Analogia (15 min)
* Mostre a tela de um roteador/switch Cisco quando o técnico acessa via terminal SSH (o menu de opções do terminal).
* Faça a pergunta disparadora: *"Por que os programas que fizemos até agora encerravam logo após a primeira digitação? Como criar um software que continua vivo até que o usuário decida sair?"*

#### 2. Live Coding Passo a Passo (45 min)
1. **Passo 1.1:** Criar a função `exibir_menu()` apenas com prints elegantes formatados com divisores `"=" * 40`.
2. **Passo 1.2:** Criar a função `main()` contendo um laço `while True`.
3. **Passo 1.3:** Capturar a opção com `opcao = input("Escolha uma opção: ").strip()`.
4. **Passo 1.4:** Escrever a árvore de decisão `if opcao == "1": ... elif ... else:`.
5. **Passo 1.5:** Criar os *stubs* (placeholders com `print("[EM CONSTRUÇÃO]")`) para que nenhuma opção quebre.
6. **Passo 1.6:** Implementar a saída segura com `break` na opção `"0"`.

#### 3. Armadilhas Comuns dos Alunos e Mediação do Professor
* **Comparação numérica x string:** Alunos costumam fazer `if opcao == 1:` (número inteiro), mas esquecem de converter o `input()` para `int`.
  > *Dica pedagógica:* Recomende comparar como texto (`"1"`, `"2"`), pois evita o erro fatal do Python caso o usuário aperte ENTER sem digitar nada.
* **Esquecer o `break`:** O menu volta a exibir infinitamente após a opção 0.
* **Identação do loop:** Código dentro do `while` sem avanço de 4 espaços.

#### 4. Checkpoint do Aluno (Critério de Conclusão da Aula 1)
O aluno deve rodar o script no terminal e verificar:
- [x] O menu surge na tela com layout limpo.
- [x] Ao digitar `9` ou texto inválido, surge aviso de erro e o menu reaparece.
- [x] Ao escolher `1`, `2`, `3` ou `4`, aparece `[EM CONSTRUÇÃO]` e o menu retorna.
- [x] Ao digitar `0`, o programa despede-se e fecha suavemente.

#### 5. Desafio Extra para Alunos Avançados
* Customizar o menu incluindo a data atual ou o nome do usuário técnico responsável pelo orçamento.

---

### 🔹 AULA 2: Entrada Segura de Dados e Previsão de Renda
* **Duração:** 90 minutos
* **Objetivo Geral:** Compreender escopo de variáveis, retorno de funções (`return`) e construir barreiras de defesa no software com `try/except`.

#### 1. Contextualização e Analogia (15 min)
* Apresente a analogia da **"Catraca de Acesso"**: ela não permite passar se o bilhete estiver inválido ou vencido; ela repete o pedido até que um bilhete válido seja inserido.
* Faça a demonstração ao vivo do "Crash": execute um script com `float(input())` e digite `"mil"` ou `"1500,50"`. Mostre o temido `ValueError: could not convert string to float`.

#### 2. Live Coding Passo a Passo (45 min)
1. **Passo 2.1:** Construir a função utilitária `obter_numero_positivo(mensagem)`.
2. **Passo 2.2:** Adicionar o bloco `try:` para a conversão `float(input(mensagem))`.
3. **Passo 2.3:** Validar regra de negócio financeira: `if valor >= 0: return valor`.
4. **Passo 2.4:** Tratar o `except ValueError:` com aviso amigável ao usuário.
5. **Passo 2.5:** Construir a função `definir_renda()` que reaproveita a função de validação e retorna a renda.
6. **Passo 2.6:** Conectar à `main()`: inicializar `renda_prevista = 0.0` e atribuir `renda_prevista = definir_renda()` na opção `"1"`.

#### 3. Armadilhas Comuns dos Alunos e Mediação do Professor
* **Esquecer o `return`:** O aluno faz o cálculo, mas a função retorna `None`. Ao tentar usar o valor na `main()`, a variável perde o dado.
* **Variável local vs global:** O aluno cria `renda` dentro de `definir_renda()` e tenta acessá-la diretamente na `main()` sem atribuir o retorno (`NameError`).
  > *Dica pedagógica:* Desenhe na lousa a metáfora da "Caixa Preta": o que entra são os parâmetros (inputs), o que sai é a esteira do `return`.

#### 4. Checkpoint do Aluno (Critério de Conclusão da Aula 2)
O aluno deve testar o programa contra erros deliberados:
- [x] Tentar digitar `"abc"`, `"quinhentos"`, `"@#"`. O sistema não deve travar com rastreamento vermelho de erro.
- [x] Tentar digitar `"-500"`. O sistema deve informar que valores negativos não são aceitos.
- [x] Digitar `"3500.50"`. O sistema confirma com `R$ 3500.50` e volta ao menu principal.

#### 5. Desafio Extra para Alunos Avançados
* Tratar a digitação de vírgula no lugar de ponto (ex: `input().replace(",", ".")`) antes da conversão para `float`.

---

### 🔹 AULA 3: Modelando Dados Compostos – Cadastro de Despesas (`list` + `dict`)
* **Duração:** 90 minutos
* **Objetivo Geral:** Aprender a estruturar registros complexos do mundo real usando dicionários (`dict`) e agregá-los dinamicamente em listas (`list`).

#### 1. Contextualização e Analogia (15 min)
* Faça um paralelo com Redes de Computadores:
  * Em uma **Tabela de Roteamento** ou **Tabela ARP**, cada linha é um registro com vários campos: IP, Máscara, Gateway, Métrica.
  * Em Python, **cada linha é um Dicionário** e a **tabela completa é uma Lista**.

#### 2. Live Coding Passo a Passo (45 min)
1. **Passo 3.1:** Na `main()`, instanciar a lista vazia: `despesas = []`.
2. **Passo 3.2:** Criar a função `adicionar_despesa(despesas)`.
3. **Passo 3.3:** Validar que o campo descrição não fique vazio: `while not descricao:`.
4. **Passo 3.4:** Reutilizar `obter_numero_positivo("Valor da despesa (R$): ")`.
5. **Passo 3.5:** Criar um submenu de 3 categorias numeradas (1 - Essencial, 2 - Estilo de Vida, 3 - Reserva) com laço de validação.
6. **Passo 3.6:** Empacotar tudo no dicionário `item = {"descricao": ..., "valor": ..., "categoria": ...}`.
7. **Passo 3.7:** Inserir na coleção com `despesas.append(item)`.

#### 3. Armadilhas Comuns dos Alunos e Mediação do Professor
* **Chaves de dicionário com nomes inconsistentes:** Usar `"Descricao"` (maiúsculo) em um lugar e `"descricao"` (minúsculo) em outro (`KeyError`).
* **Substituição em vez de anexação:** Esquecer o `.append()` e fazer `despesas = item`, transformando a lista em um único dicionário.
* **Mutabilidade:** Compreender por que a lista `despesas` passada como parâmetro para a função é alterada diretamente sem precisar de `return`.

#### 4. Checkpoint do Aluno (Critério de Conclusão da Aula 3)
- [x] O usuário entra na opção `"2"`, preenche descrição, valor e escolhe categoria.
- [x] Se deixar a descrição em branco ou com apenas espaços, o sistema cobra novamente.
- [x] Se digitar categoria inválida (ex: `4`), o sistema repete a pergunta de categoria.
- [x] O sistema emite mensagem de sucesso informando a quantidade atual de despesas cadastradas.

#### 5. Desafio Extra para Alunos Avançados
* Permitir cancelar o cadastro da despesa caso o usuário digite `"cancelar"` no campo de descrição.

---

### 🔹 AULA 4: Visualização e Iteração – Listagem Formatada em Tabela
* **Duração:** 90 minutos
* **Objetivo Geral:** Dominar a iteração sobre coleções compostas (`for .. in`), o uso de `enumerate()` e a formatação profissional de relatórios no console.

#### 1. Contextualização e Analogia (15 min)
* Mostre a saída de comandos de rede no terminal Linux/Windows: `ipconfig`, `netstat`, `arp -a`.
* Destaque: todas as ferramentas profissionais exibem informações em **colunas perfeitamente alinhadas**, o que facilita a leitura rápida humana.

#### 2. Live Coding Passo a Passo (45 min)
1. **Passo 4.1:** Criar a função `listar_despesas(despesas)`.
2. **Passo 4.2:** Inserir a cláusula de guarda: `if not despesas:` para avisar que a lista está vazia e sair com `return`.
3. **Passo 4.3:** Construir o cabeçalho alinhado com f-string:
   ```python
   print(f"{'#':<4} {'Descrição':<25} {'Categoria':<15} {'Valor (R$)'}")
   print("-" * 55)
   ```
4. **Passo 4.4:** Percorrer a lista com `enumerate(despesas, start=1)`.
5. **Passo 4.5:** Formatar cada linha da tabela puxando as chaves do dicionário `item`:
   - `indice:<4` (alinhado à esquerda em 4 espaços)
   - `item['descricao']:<25` (alinhado à esquerda em 25 caracteres)
   - `item['categoria']:<15` (alinhado à esquerda em 15 caracteres)
   - `item['valor']:>8.2f` (alinhado à direita com 2 casas decimais)
6. **Passo 4.6:** Ligar a opção `"3"` na `main()`.

#### 3. Armadilhas Comuns dos Alunos e Mediação do Professor
* **Confusão de tipos no laço:** Tentar usar `for i in range(len(despesas))` e depois fazer `despesas[i]['valor']` de forma confusa.
  > *Dica pedagógica:* Apresente o `enumerate(colecao, start=1)` como a forma mais elegante e "pythônica" de obter índice e elemento simultaneamente.
* **Tabela desalinhada:** Esquecer os modificadores `<` e `>` ou colocar nomes de despesas maiores que 25 caracteres (explique o truncamento se necessário).

#### 4. Checkpoint do Aluno (Critério de Conclusão da Aula 4)
- [x] Ao escolher a opção `"3"` antes de cadastrar despesas, aparece mensagem clara: *"Nenhuma despesa cadastrada até o momento."*
- [x] Cadastrar 3 despesas com descrições de tamanhos variados (ex: "Pão", "Aluguel do Apartamento", "Internet").
- [x] Ao listar, todos os valores em R$ aparecem alinhados pela vírgula/ponto e as categorias alinhadas em sua coluna.

#### 5. Desafio Extra para Alunos Avançados
* Truncar descrições muito longas (acima de 22 caracteres) adicionando reticências `"..."` para manter a tabela sempre esteticamente perfeita.

---

### 🔹 AULA 5: Inteligência de Negócio e Relatório Analítico (Regra 50-30-20)
* **Duração:** 90 minutos
* **Objetivo Geral:** Sintetizar lógica de programação e tomada de decisão: variáveis acumuladoras, regras de negócio financeiras, diagnósticos automatizados e finalização do projeto.

#### 1. Contextualização e Regra de Negócio (15 min)
* **Apresentação da Regra 50-30-20 (Educação Financeira):**
  * **50% Essenciais:** Gastos vitais para sobreviver (moradia, comida, saúde, contas básicas).
  * **30% Estilo de Vida:** O que torna a vida agradável (hobbies, lazer, passeios, streaming).
  * **20% Reserva Financeira / Metas:** Poupança para emergências e investimentos para o futuro.
* Explique: o papel do programador é transformar essa regra teórica em um **diagnóstico automatizado** para o usuário final!

#### 2. Live Coding Passo a Passo (45 min)
1. **Passo 5.1:** Criar a função `exibir_relatorio(renda_prevista, despesas)`.
2. **Passo 5.2:** Criar os acumuladores: `total_essencial = 0.0`, `total_estilo_vida = 0.0`, `total_reserva = 0.0`.
3. **Passo 5.3:** Iterar com `for item in despesas:` somando conforme `item["categoria"]`.
4. **Passo 5.4:** Calcular o total geral e o saldo: `saldo_restante = renda_prevista - total_gasto`.
5. **Passo 5.5:** Implementar as condicionais de situação:
   - Se saldo < 0: `ALERTA: Orçamento deficitário!`
   - Se saldo == 0: `Atenção: Saldo zerado.`
   - Se saldo > 0: `Situação: Orçamento com superávit.`
6. **Passo 5.6:** Cálculo percentual (com verificação `if renda_prevista > 0:` para **evitar divisão por zero**).
7. **Passo 5.7:** Exibição do comparativo das porcentagens reais contra as metas recomendadas.
8. **Passo 5.8:** Fechar a estrutura do programa com o padrão `if __name__ == "__main__": main()`.

#### 3. Armadilhas Comuns dos Alunos e Mediação do Professor
* **Divisão por Zero (`ZeroDivisionError`):** Se o usuário não definiu a renda (renda = 0) e tentar gerar o relatório, o cálculo `(total / renda) * 100` quebra o programa.
  > *Dica pedagógica:* Destaque a importância da verificação defensiva `if renda_prevista > 0:`.
* **Escopo das variáveis acumuladoras:** Inicializar os totais dentro do loop `for` (o que resetaria a soma a cada item) em vez de fora dele.

#### 4. Checkpoint do Aluno (Critério de Conclusão da Aula 5)
- [x] O sistema executa de ponta a ponta sem qualquer erro.
- [x] Ao definir renda de R$ 3.000,00 e lançar despesas nas 3 categorias, o relatório exibe com precisão:
  - Renda prevista
  - Total gasto
  - Saldo restante com alerta de situação
  - Porcentagens calculadas e comparadas com a meta 50-30-20.

---

## 💡 Rubrica de Avaliação Formativa do Projeto

Utilize esta rubrica para avaliar a evolução dos estudantes ao longo das fases:

| Critério | Insuficiente (D) | Em Desenvolvimento (C) | Bom (B) | Excelente (A) |
| :--- | :--- | :--- | :--- | :--- |
| **Controle de Fluxo e Menu** | O menu trava ou encerra inesperadamente. | O menu funciona, mas não trata opções inválidas de forma elegante. | Menu funcional com repetição, saída suave e tratamento de entradas inválidas. | Menu limpo, modularizado com funções, padrão `if __name__ == "__main__"`. |
| **Tratamento de Exceções & Validação** | O programa fecha com erro vermelho ao digitar letras ou valores inválidos. | Trata algumas entradas, mas com lógica duplicada em vários pontos. | Usa `try/except` e garante que não haja quebra por tipo de dados. | Função `obter_numero_positivo` genérica e reutilizável em todo o sistema. |
| **Estruturas de Dados (`list` e `dict`)** | Não usa dicionários ou usa variáveis soltas desorganizadas. | Usa dicionários mas com dificuldade de acesso a chaves ou erro de escopo. | Modela cada despesa como dicionário e armazena em lista com `.append()`. | Manipulação segura de chaves, listas dinâmicas e verificação de lista vazia. |
| **Relatórios e Regras de Negócio** | Cálculos matemáticos incorretos ou com divisão por zero. | Calcula totais mas erra porcentagens ou lógica de superávit/déficit. | Realiza todos os cálculos, somas por categoria e saldo corretamente. | Diagnóstico analítico completo, f-strings alinhadas e regra 50-30-20 perfeita. |

---

## 🚀 Desafios de Extensão (Para Feira de Ciências, Mostra Técnica ou Recuperação)

Para alunos que desejam ir além ou para um projeto integrador interdisciplinar com a área de Redes/Sistemas:

1. **Filtro de Despesas por Categoria (Opção 5 no Menu):**
   - Permitir que o usuário digite a categoria desejada e liste apenas as despesas daquele grupo com seu subtotal.
2. **Exclusão de Despesa por ID:**
   - Permitir remover uma despesa pelo número da linha exibido na listagem com `despesas.pop(indice - 1)`.
3. **Limpeza Automática de Tela:**
   - Adicionar uma função `limpar_tela()` utilizando `os.system('cls' if os.name == 'nt' else 'clear')` para deixar a interface estilo terminal limpo a cada navegação.
4. **Persistência em Arquivo CSV (Exportação):**
   - Criar uma função para salvar a lista de despesas em um arquivo `despesas.csv` utilizando apenas funções nativas do Python (`open()`, `.write()`, `.close()`).
