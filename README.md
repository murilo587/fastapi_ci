# 📚 API de Alunos com FastAPI & CI com GitHub Actions 🚀

Este é um projeto simples que utiliza **FastAPI** para criar uma API RESTful e **GitHub Actions** para automação da integração contínua (CI). O projeto inclui a validação de código e execução de testes automatizados com **Black**, **Flake8** e **Pytest**. 

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework rápido e moderno para criação de APIs.
- **Uvicorn**: Servidor ASGI de alta performance para rodar o FastAPI.
- **Pytest**: Framework para execução de testes.
- **Flake8**: Ferramenta de linting para garantir a qualidade do código.
- **Black**: Formatador de código automático para garantir estilo consistente.
- **Pydantic**: Validação de dados e criação de modelos.

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/murilo587/fastapi_ci.git
   cd fastapi_ci
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate     # Para Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Para rodar o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Para rodar os testes:
   ```bash
   pytest
   ```
6. Para verificar a formatação de código com Black:
   ```bash
   black --check .
   ```
7. Para rodar o linting com Flake8:
   ```bash
   flake8 .
   ```
## ⚙️ Funcionalidades da API

- A API possui as seguintes rotas para manipulação de dados dos alunos:

- GET /alunos: Retorna todos os alunos.

- GET /alunos/{aluno_id}: Retorna um aluno pelo ID.

- POST /alunos: Cria um novo aluno.

## 🧪 Testes

- O projeto inclui testes automatizados utilizando Pytest. Os testes cobrem:

- Listagem de alunos.

- Busca de aluno por ID.

- Criação de novo aluno.

- Validação de erro ao tentar criar um aluno com ID duplicado.

Execute os testes com:
   ```bash
    pytest
   ```

## 🔧 Integração Contínua com GitHub Actions

Este projeto possui um pipeline de CI configurado no GitHub Actions para garantir que:

- O código está formatado corretamente com Black.

- O código segue as regras de estilo com Flake8.

- Todos os testes passam com Pytest.

A integração contínua é executada automaticamente sempre que há um push ou pull request para a branch ``main``.

## 📦 Estrutura do Projeto

```bash
├── app/
│   └── main.py          # Arquivo principal com a API FastAPI
├── requirements.txt     # Dependências do projeto
├── .flake8              # Configuração do Flake8
├── pyproject.toml       # Configuração do Black
├── tests/               # Diretório de testes com Pytest
│   └── test_main.py     # Testes da API
├── .github/
│   └── workflows/       # Configuração do GitHub Actions
│       └── ci.yml       # Pipeline de CI
└── README.md            # Este arquivo
```
