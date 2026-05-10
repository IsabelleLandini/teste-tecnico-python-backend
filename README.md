# 📊 Log de Performance API

API desenvolvida com **Python** e **FastAPI** para registro de sessões de foco e análise de produtividade do usuário.

---

# Objetivo do Projeto

O objetivo desta API é permitir que o usuário registre blocos de trabalho e receba um **diagnóstico automático de produtividade**, baseado em métricas simples como:

* Nível de foco (1 a 5)
* Tempo de trabalho (minutos)
* Comentários da sessão

A partir disso, a API calcula métricas e gera feedback automático.

---

# Funcionalidades

* Registro de sessões de foco
* Persistência de dados com SQLite
* Validação de dados de entrada (nível de foco e tempo)
* Separação de regras de negócio em service layer
* Cálculo de média de foco
* Cálculo de tempo total produtivo
* Geração de feedback inteligente
* Uso de response_model para padronização de saída

---

# Tecnologias Utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

# Estrutura do Projeto

```bash
app/
├── crud.py
├── database.py
├── main.py
├── models.py
├── services.py
└── schemas.py
tests/
└── test_api.py
```

---

# Como Executar o Projeto

## 1. Instalar dependências

```bash
poetry install
```

---

## 2. Rodar a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 3. Acessar documentação

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

# Endpoints

## POST `/registro-foco`

Registra uma sessão de foco do usuário.

### Regras de validação

* `nivel_foco`: entre 1 e 5
* `tempo_minutos`: maior que 0

### Exemplo de request

```json
{
  "nivel_foco": 5,
  "tempo_minutos": 90,
  "comentario": "Estudando FastAPI",
  "categoria": "estudo"
}
```

---

## GET `/diagnostico-produtividade`

Retorna um resumo inteligente baseado nos registros salvos.

### Exemplo de response

```json
{
  "media_foco": 4,
  "tempo_total_focado": 180,
  "feedback": "Você está em uma maratona produtiva de alto nível!"
}
```

---

# Lógica do Diagnóstico

A API calcula automaticamente:

## Média de foco

- Soma dos níveis de foco dividida pela quantidade de registros

## Tempo total

- Soma de todos os minutos registrados

## Feedback automático

* Média < 3 → sugestão de pausas e menos distrações
* Média entre 3 e 4 → foco bom com espaço para melhora
* Média > 4 → alto desempenho produtivo

---

# Estrutura da Arquitetura

O projeto segue separação em camadas:

* `main.py` → rotas da API
* `crud.py` → acesso ao banco de dados
* `models.py` → definição das tabelas
* `schemas.py` → validação de dados
* `database.py` → configuração do banco

---

# Testes

Este projeto possui testes automatizados utilizando Pytest e TestClient do FastAPI.
O TestClient foi utilizado para simular requisições HTTP nos endpoints da API.

Os testes validam:

- Criação de registros de foco (POST /registro-foco)
- Validação de dados inválidos (nível de foco fora do range)
- Funcionamento do endpoint de diagnóstico com e sem registros

---

## Como rodar os testes

```bash
pytest
```

---

# Uso de Inteligência Artificial

Este projeto contou com o uso de ferramentas de Inteligência Artificial (como ChatGPT) para auxiliar no desenvolvimento.

A IA foi utilizada para:

* Apoio na estruturação do backend
* Ajuda na lógica de negócio e validações
* Explicação de conceitos técnicos
* Revisão e melhoria de código
* Apoio na documentação

Todo o código foi compreendido, revisado e implementado manualmente durante o desenvolvimento.

---

# 👩‍💻 Desenvolvido por

Isabelle Landini
