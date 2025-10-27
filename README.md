# 📚 API de Alunos com FastAPI & CI com GitHub Actions 🚀

Este é um projeto simples que utiliza **FastAPI** para criar uma API RESTful e **GitHub Actions** para automação da integração contínua (CI). O projeto inclui a validação de código e execução de testes automatizados com **Black**, **Flake8** e **Pytest**. 

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework rápido e moderno para criação de APIs.
- **Uvicorn**: Servidor ASGI de alta performance para rodar o FastAPI.
- **Pytest**: Framework para execução de testes.
- **Flake8**: Ferramenta de linting para garantir a qualidade do código.
- **Black**: Formatador de código automático para garantir estilo consistente.
- **Pydantic**: Validação de dados e criação de modelos.

## 🆕 Funcionalidades da Branch `feat/pytest-fixture-mock`

A branch **`feat/pytest-fixture-mock`** introduziu melhorias significativas no processo de testes, garantindo que as chamadas à API externa sejam **simuladas** (mocked) e que a organização dos testes seja mais **modular e reutilizável** por meio de **Fixtures**. As principais mudanças e funcionalidades adicionadas foram:

#### 1. **Testes com Fixtures**
   - A **Fixture** foi introduzida para fornecer dados simulados que podem ser reutilizados em múltiplos testes, tornando o código dos testes mais organizado e eficiente.
   - A **Fixture** criada no arquivo `tests/test_main.py` simula um **usuário** para ser utilizado nos testes de criação e listagem de usuários.
   - **Exemplo de Fixture**:
     ```python
     @pytest.fixture
     def mock_usuario():
         return {"id": 1, "name": "Usuário Teste", "email": "teste@exemplo.com"}
     ```

#### 2. **Mocks para Simulação da API Externa**
   - Utilizando **`unittest.mock.patch`**, a branch **`feat/pytest-fixture-mock`** implementou a simulação (mocking) das requisições HTTP feitas com o **httpx**.
   - **Mocks** foram aplicados em todos os testes relacionados à API externa para **evitar chamadas reais** e garantir que os testes sejam executados de forma controlada.
   - **Exemplo de Mock**:
     ```python
     @patch("app.main.httpx.get")
     def test_listar_usuarios_sucesso(mock_get, mock_usuario):
         mock_get.return_value.status_code = 200
         mock_get.return_value.json.return_value = [mock_usuario]
         response = client.get("/usuarios")
         assert response.status_code == 200
     ```

#### 3. **Testes Independentes de API Externa**
   - Agora os testes não dependem mais de chamadas reais à API externa. Isso permite que os testes sejam executados mais rapidamente e sem dependências externas.
   - O uso de mocks simula respostas da API externa (como `200`, `404` e `500`), garantindo que diferentes cenários sejam testados.

#### 4. **Cobertura Abrangente de Testes**
   - Com a introdução de **Mocks** e **Fixtures**, todos os cenários importantes foram cobertos:
     - **Sucesso** nas operações de listar, buscar e criar usuários.
     - **Falhas esperadas**, como erros de **404** (não encontrado) e **502** (erro ao acessar a API externa).

#### 5. **Exclusão de Dependências Reais**
   - A branch **`feat/pytest-fixture-mock`** removeu a necessidade de interagir com a API externa real durante os testes, melhorando a confiabilidade dos testes ao eliminar fatores externos.


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
