# Planejamento do Sistema de Calculadora - Django 6

Este documento descreve as etapas de desenvolvimento, diretrizes, arquitetura e instruções para o sistema de calculadora baseado em Django 6 com uma API REST e uma interface web moderna e responsiva.

---

## 1. Diretivas da Aplicação

### 1.1. Backend (Django 6.0)
* **Arquitetura RESTful**: Endpoints específicos para processamento de operações matemática e manipulação do histórico.
* **Persistência de Dados**: Armazenamento do histórico de operações realizadas (usando banco de dados SQLite padrão do Django).
* **Robustez e Validação**: Tratamento estrito de erros matemáticos (como divisão por zero, números imaginários ou transbordamento) e entradas inválidas no payload da requisição.
* **Compatibilidade**: Desenvolvido sob a versão estável do Django 6.0 e Python 3.14.

### 1.2. Frontend (Single Page Application - SPA)
* **Aparência Premium (WOW Factor)**: Interface baseada em Glassmorfismo e Neumorfismo escuro (Dark Mode por padrão), com fontes modernas da Google Fonts (como 'Orbitron' para o display e 'Outfit' para os botões).
* **Interatividade & Animações**: Micro-animações no clique dos botões, transições suaves e feedback sonoro/visual para simular um dispositivo real.
* **Suporte Completo a Teclado**: Atalhos para operações usuais (números, operadores, `Enter` para resultado, `Escape` ou `BackSpace` para limpar).
* **Histórico em Tempo Real**: Painel interativo acoplado para visualizar e reutilizar cálculos anteriores diretamente no display.

---

## 2. Estrutura de Endpoints da API REST

A API operará inteiramente sobre JSON. Os seguintes endpoints serão expostos:

| Método | Endpoint | Descrição | Payload Esperado | Resposta (Sucesso) |
|---|---|---|---|---|
| `POST` | `/api/calculate/` | Realiza um cálculo matemático, salva no banco e retorna o resultado. | `{"expression": "2 + 2"}` ou `{"num1": 10, "num2": 5, "operation": "add"}` | `{"success": true, "result": "4", "id": 1}` |
| `GET` | `/api/history/` | Retorna a lista dos últimos cálculos realizados (limite de 10 registros). | N/A | `[{"id": 1, "expression": "2 + 2", "result": "4", "timestamp": "..."}]` |
| `DELETE` | `/api/history/clear/` | Limpa todos os registros do histórico no banco de dados. | N/A | `{"success": true, "message": "Histórico limpo."}` |

---

## 3. Etapas de Desenvolvimento

A implementação está estruturada nas seguintes etapas consecutivas:

### Etapa 1: Setup do Ambiente e Estruturação do Projeto Django
1. Criação do projeto Django (`django-admin startproject django_calculadora .`).
2. Criação do app `calculator` (`python manage.py startapp calculator`).
3. Configuração dos arquivos estáticos, templates e definição do `ALLOWED_HOSTS` no `settings.py`.

### Etapa 2: Implementação do Banco de Dados e Modelos
1. Definição do modelo `Calculation` para armazenar `expression`, `result` e `timestamp`.
2. Criação e execução das migrações do banco de dados.

### Etapa 3: Desenvolvimento da API REST no Django 6
1. Escrita das funções de visualização (views) para processar cálculos de forma segura usando análise sintática segura (evitando o uso inseguro de `eval()`).
2. Implementação dos endpoints `/api/calculate/`, `/api/history/` e `/api/history/clear/` com suporte a CSRF seguro.
3. Mapeamento das URLs no arquivo `urls.py`.

### Etapa 4: Criação do Frontend Premium
1. Estruturação do template HTML5 semântico com display de LED e painel de histórico.
2. Escrita dos estilos em CSS (dentro de `static/css/styles.css`) aplicando gradientes sutis, sombras realistas de Neumorfismo e efeitos de desfoque de fundo (Glassmorphism).
3. Implementação da lógica em JavaScript (`static/js/calculator.js`) para capturar entradas de botões e teclado, disparar chamadas assíncronas (`fetch`) para a API REST e renderizar os resultados.

### Etapa 5: Testes, Refinamentos e Validação
1. Verificação de cenários de erro (ex: `"1 / 0"`, `"10.2 ++ 2"`, inputs maliciosos).
2. Validação visual em telas de diferentes tamanhos (responsividade).
3. Testes de usabilidade usando o teclado numérico do computador.

---

## 4. Instruções de Instalação e Execução

### Pré-requisitos
* Python 3.12+ (Executando com Python 3.14 no ambiente atual)
* Django 6.0+

### Passo a Passo

1. **Ativar o Ambiente Virtual:**
   ```bash
   source venv/bin/activate
   ```

2. **Instalar Dependências:**
   *(O Django 6 já foi instalado no ambiente).*
   ```bash
   pip install django
   ```

3. **Executar as Migrações do Banco de Dados:**
   ```bash
   python manage.py migrate
   ```

4. **Iniciar o Servidor de Desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

5. **Acesse no Navegador:**
   Abra `http://127.0.0.1:8000/` para interagir com a calculadora.
