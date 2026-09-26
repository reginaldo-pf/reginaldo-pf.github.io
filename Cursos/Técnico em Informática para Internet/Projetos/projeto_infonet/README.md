# Calculadora REST - Django 6

Uma aplicação web moderna e interativa de calculadora desenvolvida com **Django 6.0**, **Python 3.14** e **API REST** para processamento das operações matemáticas e persistência do histórico de cálculos.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente:

### 1. Ativar o Ambiente Virtual
O ambiente virtual já está pré-configurado no projeto. Ative-o com o comando:
```bash
source venv/bin/activate
```

### 2. Rodar as Migrações do Banco de Dados
Garante que a tabela do histórico de cálculos seja criada no banco de dados SQLite:
```bash
python manage.py migrate
```

### 3. Executar a Suíte de Testes (Opcional)
Execute os testes unitários e de integração para validar a calculadora:
```bash
python manage.py test
```

### 4. Iniciar o Servidor de Desenvolvimento
Inicie o servidor local do Django:
```bash
python manage.py runserver
```

### 5. Acessar a Aplicação
Abra seu navegador e acesse:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📄 Planejamento e Diretrizes

As informações detalhadas sobre a arquitetura da API, etapas de desenvolvimento realizadas e decisões de design estão descritas no arquivo:
👉 [calculadora_planejamento.md](file:///home/reginaldo-fernandes/projeto_infonet/calculadora_planejamento.md)

## 🛠️ Tecnologias Utilizadas

* **Backend**: Django 6.0.7 & Python 3.14
* **Banco de Dados**: SQLite3 (gerenciado pelo ORM do Django)
* **Frontend**: HTML5, CSS3 (com Glassmorphism/Dark Mode), JavaScript ES6 (Fetch API para consumo REST)
* **Segurança**: AST (Abstract Syntax Tree) para análise sintática segura das expressões aritméticas, proteção contra CSRF em requisições assíncronas.
