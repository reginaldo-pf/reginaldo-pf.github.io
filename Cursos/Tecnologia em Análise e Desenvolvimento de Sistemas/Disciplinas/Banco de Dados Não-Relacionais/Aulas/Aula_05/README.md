# Aula 05: Redis na Prática — Padrão Cache-Aside, Performance e Expiração (TTL)

* **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
* **Componente Curricular:** Banco de Dados Não-Relacionais (ADS16)  
* **Docente Responsável:** Prof. Me. Reginaldo Fernandes  
* **Semestre Letivo:** 2026.2  
* **Data da Aula:** 20 de Outubro de 2026 (Terça-feira)  
* **Carga Horária:** 2 h/a (120 minutos)  
* **Módulo:** Unidade II (N1) — O Modelo Chave-Valor e Arquiteturas In-Memory  
* **Vídeo Base do Guia Prático:** [CACHE-ASIDE: Escalabilidade, Performance e Arquitetura de Software (Renato Augusto)](https://www.youtube.com/watch?v=vRO0UfvsbDw)

---

## 🎯 Competências e Objetivos Práticos

- [x] Compreender por que consultas repetidas (`SELECT`) aos mesmos dados estrangulam o banco de dados relacional em picos de acesso (como uma Black Friday).
- [x] Comparar a velocidade das camadas de armazenamento: HD Magnético ($\approx 10\text{ ms}$), SSD ($\approx 100\text{ }\mu\text{s}$) e Memória RAM com Redis ($\approx 100\text{ ns}$ via protocolo RESP).
- [x] Implementar o padrão **Cache-Aside** no endpoint `/categories/featured` do e-commerce **ShopGrids** utilizando `GET` e `SET`.
- [x] Reproduzir e diagnosticar o **Problema da Inconsistência de Dados** quando o banco de dados é atualizado e o cache não possui expiração.
- [x] Implementar a invalidação automática por tempo (**TTL — Time To Live**) utilizando `SETEX` (`r.setex("featured_categories", 20, ...)`).
- [x] Avaliar os **3 Critérios de Ouro** para decidir quando cachear um dado (alta frequência de leitura, baixa frequência de mutação e tolerância à consistência eventual).

---

## 📁 Estrutura de Arquivos da Aula 05

- [`tutorial_construcao_passo_a_passo.md`](tutorial_construcao_passo_a_passo.md): **Roteiro Prático do Aluno (Passo a Passo Autônomo)** — guia completo com código comentado linha por linha e explicação da função de cada instrução para o estudante seguir sem depender da videoaula.
- [`roteiro_privado_professor_videoaula.md`](roteiro_privado_professor_videoaula.md): **🔒 Roteiro Privado do Professor (Gravação da Videoaula)** — guia de direção, falas sugeridas para a câmera, ações de tela e código linha a linha para gravação da aula.
- [`index.html`](index.html): Portal web didático da Aula 05 com o estudo de caso, guia prático passo a passo, slides em PDF e exercícios.
- [`plano_de_aula.md`](plano_de_aula.md): Roteiro pedagógico da aula.
- `codigo/`:
  - [`criar_banco.py`](codigo/criar_banco.py): Script do Passo 3 do roteiro que cria o banco `shopgrids.db` e popula a tabela `categories`.
  - [`app.py`](codigo/app.py): Aplicação Flask + SQLite (`shopgrids.db`) + Redis implementando a rota `/categories/featured` e rotas de atualização da tabela `categories`.
  - [`templates/index.html`](codigo/templates/index.html): Simulador visual em duas colunas (Front-end/Postman na esquerda vs. Tabela `categories` do Banco SQL e contador de TTL do Redis na direita).
  - [`demonstracao_aula05.ipynb`](codigo/demonstracao_aula05.ipynb): Jupyter Notebook interativo com as 4 etapas práticas do padrão Cache-Aside e TTL.
  - [`iniciar.sh`](codigo/iniciar.sh): Script utilitário para verificar o Redis e subir o servidor na porta `5000`.
  - [`docker-compose.yml`](codigo/docker-compose.yml): Configuração para subir o Redis via Docker.
  - [`requirements.txt`](codigo/requirements.txt): Dependências Python (`flask` e `redis`).
- `materiais/`:
  - [`main.pdf`](materiais/main.pdf) e arquivos `.tex` da apresentação em slides.

---

## 🚀 Como Executar o Exemplo Prático em Sala de Aula

1. **Certifique-se de que o Redis está rodando:**
   ```bash
   redis-server
   # ou: docker compose -f codigo/docker-compose.yml up -d
   ```
2. **Inicie a aplicação ShopGrids:**
   ```bash
   cd codigo
   ./iniciar.sh
   # ou: python app.py
   ```
3. **Teste pelo Navegador ou pelo Terminal (`curl` / Postman):**
   * **Painel Interativo:** Acesse `http://localhost:5000`
   * **Endpoint do Vídeo:** `curl -s http://localhost:5000/categories/featured | jq .`
