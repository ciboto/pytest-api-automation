# 🧪 Projeto de Testes Automatizados de API com Pytest

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Pytest](https://img.shields.io/badge/Pytest-Tested-brightgreen?style=for-the-badge&logo=pytest)
![License](https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey?style=for-the-badge)
![CI/CD](https://img.shields.io/github/actions/workflow/status/ciboto/pytest-api-automation/python-tests.yml?style=for-the-badge)

> Projeto com testes automatizados de API utilizando `pytest`, geração de relatórios HTML e pipeline de CI/CD no GitHub Actions.

---

## 📂 Estrutura do Projeto
```
pytest-api-automation/
├── .github/workflows/      # Pipeline de CI/CD
│ └── python-tests.yml
├── reports/                # Relatórios HTML
│ └── report.html
├── tests/                  # Testes automatizados separados por metodos
│ └── test_delete_api.py
│ └── test_get_api.py
│ └── test_patch_api.py
│ └── test_post_api.py
│ └── test_put_api.py
├── requirements.txt         # Dependências
├── pytest.ini               # Configuração do pytest
└── README.md
```
---

## 🚀 Tecnologias

- Python 3.11+
- [Pytest](https://docs.pytest.org/)
- [Requests](https://requests.readthedocs.io/)
- [pytest-html](https://pypi.org/project/pytest-html/)
- GitHub Actions

---

## 🔧 Instalação
1. Clone o repositório:

```bash
git clone https://github.com/ciboto/pytest-api-automation.git
cd pytest-api-automation
```

2. Crie e ative o ambiente virtual:
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```
---
## ✅ Executando os Testes

- Testes simples:
```bash
pytest
```

- Testes com relatório HTML:
```bash
pytest --html=reports/report.html --self-contained-html
```
Abra o arquivo `reports/report.html` em seu navegador para visualizar o resultado.
![Report PW Preview](assets/pytest-report.PNG)
---

## ⚙️ CI/CD com GitHub Actions
Este projeto já possui um workflow configurado em .github/workflows/python-tests.yml.

Ele será executado automaticamente em:
- Pull requests
- Workflow dispatch (manual)

E gera um relatório HTML como artefato do pipeline.
```yaml
name: Python API Tests

on:
  push:
  pull_request:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Run tests with report
        run: |
          source venv/bin/activate
          pytest --html=reports/report.html --self-contained-html

      - name: Upload test report artifact
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: reports/report.html
```
---
## ⚖️ Licença
Este projeto está licenciado sob a [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) - Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
