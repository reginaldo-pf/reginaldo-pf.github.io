# Roteiro de Live Coding e Gravação de Vídeo (Guia do Professor)
## Etapa 3 (GUI): Cadastro de Despesas, Listagem Rolável e Persistência em JSON

* **Curso:** Técnico em Redes de Computadores – IFCE Campus Tauá
* **Disciplina:** Lógica de Programação com Python
* **Professor:** Reginaldo Fernandes
* **Formato Metodológico:** **Construção Incremental Interativa (Visual ➔ Teste ➔ Função ➔ Teste)** — ponto de partida exato no arquivo [projetinho/gui_main.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/projetinho/gui_main.py) finalizado na aula passada.
* **Arquivo Gabarito de Apoio:** [etapas/etapa3_gui_customtkinter.py](file:///home/reginaldo-fernandes/Aulas/Cursos/Técnico em Redes de Computadores/Disciplinas/Lógica de Programação/Aulas/projeto_final/etapas/etapa3_gui_customtkinter.py)

---

## 🧭 Decisão Arquitetural: Qual a Melhor Opção de Armazenamento (JSON vs. SQLite)?

Antes de iniciar a gravação/aula, aqui está a análise técnica e pedagógica para você usar e responder à turma:

> [!IMPORTANT]
> **Veredito para este Projeto: JSON (`import json`) é de longe a melhor escolha!**
>
> | Critério | **JSON (`json`) — Recomendado ✅** | **SQLite (`sqlite3`)** |
> | :--- | :--- | :--- |
> | **Alinhamento com a Disciplina** | **100% Direto:** Em Python, um arquivo JSON tem **exatamente a mesma sintaxe** de Listas (`[]`) e Dicionários (`{}`) que estamos ensinando! | Exige ensinar outra linguagem (`CREATE TABLE`, `INSERT INTO`, `SELECT`) e cursores, desviando o foco de Lógica de Programação. |
> | **Inspeção Visual pelo Aluno** | O aluno clica em `dados_financeiros.json` no VS Code e **lê seus próprios dados em texto aberto**, vendo sua lista de dicionários salva no disco! | Gera um arquivo binário `.db` que o aluno não consegue ler abrindo no editor sem extensões extras. |
> | **Tamanho do Código (Mínimo)** | Apenas **2 linhas** para salvar (`json.dump`) e **2 linhas** para ler (`json.load`). | Exige abrir conexão, criar cursor, criar tabela no início, fazer `commit()` e fechar conexão. |
> | **Conexão com Redes de Computadores** | JSON é o padrão universal de **APIs Web, automação de redes (Ansible/RESTCONF) e logs estruturados**. | Mais voltado para sistemas transacionais pesados e bancos embarcados. |

---

## 🎬 CENA 1: Preparando a Área Rolável de Despesas (`CTkScrollableFrame`)
*(Foco Visual: Transformar o aviso estático da direita em um container com barra de rolagem automática)*

### 🎙️ Roteiro de Fala / Contextualização:
* *"Pessoal, na aula passada deixamos um texto provisório (`lbl_placeholder_lista`) no centro do painel de despesas. Mas pensem comigo: se o usuário cadastrar 30 despesas no mês, elas vão caber na altura da tela? Não! Precisamos de uma caixa com **barra de rolagem automática** (`CTkScrollableFrame`)."*

### 1.1 O que alterar no final do `gui_main.py` (Na seção `5.2 - Painel Central`):
Localize onde estava o `lbl_placeholder_lista` (linhas 228 a 239 do `gui_main.py` atual) e **substitua** pelo `CTkScrollableFrame`:

```python
# Substitua o antigo lbl_placeholder_lista por este bloco rolável:
frame_lista_scroll = ctk.CTkScrollableFrame(frame_despesas, fg_color="transparent")
frame_lista_scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))
```

### 🧪 Checkpoint de Teste 1 (Executar ao vivo!):
* Rode `python gui_main.py`.
* **O que mostrar na tela:** Mostre que dentro do painel `LISTA DE DESPESAS REGISTRADAS` agora existe uma área com uma discreta barra de rolagem (`scrollbar`) na lateral direita, pronta para receber dezenas de linhas!

---

## 🎬 CENA 2: Desenhando a Lista na Tela (`atualizar_lista_visual`)
*(Foco: Criar a função que lê a lista `despesas` e desenha na área rolável — e já testar com um item de teste!)*

### 2.1 O que adicionar no bloco de funções no topo do arquivo:
Logo abaixo de `renda_prevista = 0.0`, crie a lista `despesas = []` e a função `atualizar_lista_visual()`:

```python
renda_prevista = 0.0
despesas = []  # Lista que guardará os dicionários de cada despesa


def atualizar_lista_visual():
    """Limpa o painel de listagem e redesenha todas as despesas da lista."""
    # 1. Remove os itens visuais antigos antes de redesenhar (evita duplicar na tela!)
    for widget in frame_lista_scroll.winfo_children():
        widget.destroy()

    # 2. Se a lista estiver vazia, mostra o aviso amigável
    if not despesas:
        lbl_vazio = ctk.CTkLabel(
            frame_lista_scroll,
            text="🚧 Nenhuma despesa cadastrada até o momento.\nClique em '2 - Adicionar Despesa' no menu lateral.",
            font=ctk.CTkFont(size=14),
            text_color="gray60",
            justify="center"
        )
        lbl_vazio.pack(pady=40)
        return

    # 3. Percorre a lista de dicionários e cria uma faixa visual para cada gasto
    for indice, item in enumerate(despesas, start=1):
        linha = ctk.CTkFrame(frame_lista_scroll, corner_radius=6, fg_color="gray17")
        linha.pack(fill="x", pady=3, padx=5)

        texto_linha = (
            f"{indice:<5} "
            f"{item['descricao'][:35]:<38} "
            f"{item['categoria']:<22} "
            f"R$ {item['valor']:>9.2f}"
        )

        lbl_item = ctk.CTkLabel(
            linha,
            text=texto_linha,
            font=ctk.CTkFont(family="monospace", size=12),
            anchor="w"
        )
        lbl_item.pack(fill="x", padx=10, pady=6)
```

E chame `atualizar_lista_visual()` no final do arquivo, uma linha **antes** de `if __name__ == "__main__":`:

```python
atualizar_lista_visual()

if __name__ == "__main__":
    janela.mainloop()
```

### 🎙️ Roteiro de Fala / Explicação Didática:
* **Por que limpamos com `winfo_children()` e `widget.destroy()`?** *"Se a lista tinha 2 itens e adicionamos o 3º, se não apagarmos os desenhos antigos antes de rodar o `for`, o programa desenharia os 2 primeiros de novo embaixo, ficando com 5 linhas na tela! Por isso limpamos a lousa e redesenhamos a lista atualizada."*
* **Alinhamento perfeito com `monospace` e `<38`:** *"Lembram que o cabeçalho usa fonte `monospace` (onde toda letra tem a mesma largura)? Na f-string usamos `:<38` (alinha à esquerda em 38 espaços) e `:>9.2f` (alinha os reais à direita com 2 casas decimais) para que as colunas batam milimetricamente com o cabeçalho!"*

### 🧪 Checkpoint de Teste 2 (Executar ao vivo!):
1. Rode `python gui_main.py` com `despesas = []` vazia ➔ Mostre que o aviso `"🚧 Nenhuma despesa cadastrada..."` aparece dentro da caixa rolável.
2. **Truque para encantar no vídeo/aula:** Coloque temporariamente 1 dicionário dentro de `despesas = [{"descricao": "Internet Fibra", "valor": 110.0, "categoria": "Essencial"}]` e rode! Os alunos verão imediatamente a primeira linha de tabela renderizada na tela! Depois volte para `despesas = []`.

---

## 🎬 CENA 3: Criando a Subjanela de Formulário (`CTkToplevel`) no Botão 2
*(Foco Visual primeiro: Abrir uma janelinha com 3 campos — Descrição, Valor e Categoria)*

### 🎙️ Roteiro de Fala / Explicação Didática:
* *"Para cadastrar a Receita na aula passada, usamos o `CTkInputDialog` porque ela pedia apenas **1 informação** (o valor). Mas uma Despesa precisa de **3 informações**: Descrição (texto), Valor (número) e Categoria (Essencial, Estilo de Vida ou Reserva). Abrir 3 janelinhas seguidas seria horrível para o usuário! Então vamos usar o `ctk.CTkToplevel(janela)` para abrir uma **subjanela de formulário completa**!"*

### 3.1 O que colocar dentro da função `adicionar_despesa()` (Apenas o Visual primeiro!):
Substitua a função `adicionar_despesa()` antiga por esta estrutura visual:

```python
def adicionar_despesa():
    """Abre uma subjanela de formulário (CTkToplevel) para cadastrar uma nova despesa."""
    popup = ctk.CTkToplevel(janela)
    popup.title("2 - Nova Despesa")
    popup.geometry("400x380")
    popup.resizable(False, False)
    popup.transient(janela)  # Mantém o pop-up sempre na frente da janela principal
    popup.grab_set()         # Trava os cliques apenas no pop-up até o usuário fechar

    # Campo 1: Descrição (Caixa de texto CTkEntry)
    ctk.CTkLabel(popup, text="Descrição da Despesa:", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(20, 5)
    )
    entry_descricao = ctk.CTkEntry(popup, placeholder_text="Ex: Conta de Internet, Aluguel...")
    entry_descricao.pack(fill="x", padx=25)

    # Campo 2: Valor (Caixa de texto CTkEntry)
    ctk.CTkLabel(popup, text="Valor da Despesa (R$):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    entry_valor = ctk.CTkEntry(popup, placeholder_text="Ex: 120.50")
    entry_valor.pack(fill="x", padx=25)

    # Campo 3: Categoria (Menu Dropdown CTkOptionMenu)
    ctk.CTkLabel(popup, text="Categoria (Regra 50-30-20):", font=ctk.CTkFont(weight="bold")).pack(
        anchor="w", padx=25, pady=(15, 5)
    )
    combo_categoria = ctk.CTkOptionMenu(
        popup,
        values=["Essencial", "Estilo de Vida", "Reserva"]
    )
    combo_categoria.pack(fill="x", padx=25)

    # Rótulo para exibir erros de validação dentro do próprio pop-up
    lbl_erro_popup = ctk.CTkLabel(popup, text="", text_color="#e74c3c", font=ctk.CTkFont(size=12))
    lbl_erro_popup.pack(pady=(10, 0))

    # Botão Salvar (Ainda sem command para testarmos o visual!)
    btn_salvar = ctk.CTkButton(
        popup,
        text="💾 Salvar Despesa",
        height=38,
        fg_color="#27ae60",
        hover_color="#1e8449"
    )
    btn_salvar.pack(fill="x", padx=25, pady=(15, 20))
```

### 💡 Informações Extras sobre os novos componentes (`CTkToplevel`, `CTkEntry`, `CTkOptionMenu`):
1. **Para que servem `popup.transient(janela)` e `popup.grab_set()`?**
   * Sem `transient(janela)`, se o usuário clicar fora do pop-up, a janelinha se esconde atrás da janela grande maximizada e o aluno acha que o programa travou!
   * O `grab_set()` transforma a subjanela em um **Modal**: enquanto o usuário não terminar de cadastrar ou fechar a janelinha, ele não consegue clicar em outros botões lá atrás (evitando abrir 10 janelas repetidas!).
2. **Por que usar `CTkOptionMenu` para a Categoria?**
   * No terminal o usuário podia digitar `"4"` ou `"essencial"` errado e precisávamos de um `while True` para validar. Com a caixinha de seleção (`CTkOptionMenu`), o usuário **só pode escolher uma das 3 opções oficiais** (`"Essencial"`, `"Estilo de Vida"`, `"Reserva"`). Zero chance de erro humano!

### 🧪 Checkpoint de Teste 3 (Executar ao vivo!):
* Rode `python gui_main.py` e clique no botão **`2 - Adicionar Despesa`**.
* **O que mostrar na tela:** A subjanela de formulário abre no centro da tela com os textos de ajuda (`placeholder_text`), o menu dropdown de categorias funcionando e o botão verde `💾 Salvar Despesa`.

---

## 🎬 CENA 4: Validando e Salvando a Despesa na Lista (`confirmar_cadastro`)
*(Foco Funcional: Ler os 3 campos, validar, criar o Dicionário, dar `.append()` na Lista e atualizar a tabela na hora!)*

### 4.1 O que adicionar dentro de `adicionar_despesa()` (Logo antes do `btn_salvar`):

```python
    def confirmar_cadastro():
        descricao = entry_descricao.get().strip()
        valor_texto = entry_valor.get().strip().replace(",", ".")
        categoria = combo_categoria.get()

        # 1. Valida se a descrição não está em branco
        if not descricao:
            lbl_erro_popup.configure(text="❌ A descrição não pode ficar vazia!")
            return

        # 2. Valida se o valor é numérico e positivo
        try:
            valor = float(valor_texto)
            if valor < 0:
                lbl_erro_popup.configure(text="❌ O valor não pode ser negativo!")
                return
        except ValueError:
            lbl_erro_popup.configure(text="❌ Digite um valor numérico válido!")
            return

        # 3. Empacota os 3 dados em um Dicionário e guarda na Lista!
        nova_despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }
        despesas.append(nova_despesa)

        # 4. Redesenha a tabela lá no painel direito e fecha o pop-up!
        atualizar_lista_visual()
        lbl_status.configure(
            text=f"✅ Despesa '{descricao}' (R$ {valor:.2f}) adicionada! Total: {len(despesas)}",
            text_color="#2ecc71"
        )
        popup.destroy()
```

E adicione `, command=confirmar_cadastro` no `btn_salvar` logo abaixo!
Aproveite também para atualizar a função `listar_despesas()` (Botão 3) para chamar `atualizar_lista_visual()` e mostrar quantas despesas existem.

### 🧪 Checkpoint de Teste 4 (Executar ao vivo!):
1. Rode o programa e clique em `2 - Adicionar Despesa`.
2. Clique em **Salvar** deixando vazio ➔ Mostre o aviso vermelho `❌ A descrição não pode ficar vazia!` dentro do pop-up.
3. Preencha `Aluguel`, valor `1200`, categoria `Essencial` e clique em **Salvar** ➔ O pop-up fecha sozinho e a linha **`1   Aluguel   Essencial   R$ 1200.00`** aparece instantaneamente na tabela da direita!
4. Cadastre uma 2ª despesa (`Cinema`, `65,50`, `Estilo de Vida`) e mostre ela entrando na linha `2`.
5. **Agora provoque a dor da falta de persistência:** Feche a janela no `X` e abra o programa de novo!
   * **Pergunta dramática para a turma/vídeo:** *"Ué?! Cadê a nossa Receita e as nossas 2 Despesas?! Sumiram todas! Por quê? Porque estavam apenas na memória RAM! Vamos resolver isso agora em menos de 15 linhas salvando tudo em disco!"*

---

## 🎬 CENA 5: A Persistência Mínima em Arquivo JSON (`salvar_dados` e `carregar_dados`)
*(Foco Final: Explicar de forma simples e direta como salvar e carregar a Receita e as Despesas no computador)*

### 🎙️ Roteiro de Fala / Explicação Mínima sobre Armazenamento:
* *"Como fazemos para o computador lembrar da nossa variável `renda_prevista` e da nossa lista `despesas` quando desligamos o programa? Precisamos gravar esses dados no disco rígido (SSD/HD)."*
* *"Em Python, a forma mais limpa e direta para salvar listas e dicionários é o formato **JSON** (que já vem instalado no Python com `import json`). Ele pega o nosso dicionário da memória RAM e escreve num arquivo de texto `.json` usando `json.dump()`, e quando o programa abre, ele lê de volta com `json.load()`!"*

### 5.1 Passo A – Importar `json` e `os` na linha 1 do arquivo:

```python
import json
import os
import customtkinter as ctk
```

### 5.2 Passo B – Criar as duas funções mínimas de arquivo (logo abaixo de `despesas = []`):

```python
ARQUIVO_DADOS = "dados_financeiros.json"
renda_prevista = 0.0
despesas = []


def salvar_dados():
    """Guarda a receita e a lista de despesas dentro do arquivo JSON."""
    pacote = {
        "renda_prevista": renda_prevista,
        "despesas": despesas
    }
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(pacote, arquivo, indent=4, ensure_ascii=False)


def carregar_dados():
    """Lê o arquivo JSON quando o programa abre (se o arquivo já existir)."""
    global renda_prevista, despesas

    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                pacote = json.load(arquivo)
                renda_prevista = pacote.get("renda_prevista", 0.0)
                despesas = pacote.get("despesas", [])
        except Exception:
            pass
```

### 5.3 Passo C – Onde chamar `salvar_dados()` e `carregar_dados()`? (Apenas 3 lugares!):
1. **Dentro de `cadastrar_receita()`:** Logo abaixo de `renda_prevista = valor`, adicione uma linha:
   ```python
   salvar_dados()
   ```
2. **Dentro de `confirmar_cadastro()` (em `adicionar_despesa`):** Logo abaixo de `despesas.append(nova_despesa)`, adicione uma linha:
   ```python
   salvar_dados()
   ```
3. **No final do arquivo (antes do `if __name__ == "__main__":`):** Carregue os dados assim que a janela terminar de ser montada:
   ```python
   carregar_dados()
   lbl_valor_receita.configure(text=f"R$ {renda_prevista:.2f}")
   atualizar_lista_visual()

   if __name__ == "__main__":
       janela.mainloop()
   ```

### 🧪 Checkpoint Final de Teste 5 (O Gran Finale do Vídeo/Aula!):
1. Rode `python gui_main.py`.
2. Cadastre uma Receita de `R$ 3500.00` e adicione 2 Despesas (`Internet - R$ 110.00` e `Supermercado - R$ 650.00`).
3. **Mostre no explorador de arquivos do VS Code:** Um arquivo chamado `dados_financeiros.json` acabou de nascer sozinho! Clique nele e mostre para a turma como os dados estão salvos lá dentro de forma legível.
4. **Feche o programa completamente** (`0 - Sair do Sistema`).
5. **Abra o programa de novo** (`python gui_main.py`) ➔ A janela já abre exibindo automaticamente **`R$ 3500.00`** no Resumo de Receita e as **2 despesas listadas na tabela**!
