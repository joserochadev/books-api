# 📚 Books API

Books API é uma aplicação para gerenciar um catálogo de livros, desenvolvida em Python com Django e Django Rest Framework (DRF).

## ✨ Funcionalidades

- Gerenciar livros com os seguintes campos obrigatórios: título, autor, ano de publicação e ISBN.
- Retornar todos os livros cadastrados.
- Exibir os detalhes de um livro específico.
- Adicionar e remover livros.
- Prevenir o cadastro de livros com ISBN duplicado.

## 🛠️ Tecnologias Utilizadas

- **Python** 3.10+
- **Django** 4.2+
- **Django Rest Framework** 3.14+
- **SQLite** (banco de dados padrão)

---

## 🚀 Como Rodar o Projeto

Clone o repositório

```bash
git clone https://github.com/joserochadev/books-api.git
cd books-api
```

Crie e ative um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Configure o banco de dados
Crie as migrações e aplique-as:

```bash
python manage.py makemigrations
python manage.py migrate
```

Popule o banco com dados de exemplo (opcional)
Execute o comando para rodar o script de seed:

```bash
python manage.py seed
```

Inicie o servidor local

```bash
python manage.py runserver
```

Acesse a API em: http://127.0.0.1:8000/

---

## 📜 Endpoints da API

### 📚 Livros

| Método   | Endpoint       | Descrição                            | Exemplo de Payload (se aplicável)                                                                   |
| -------- | -------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------- |
| `GET`    | `/books/`      | Retorna todos os livros cadastrados. | -                                                                                                   |
| `GET`    | `/books/<id>/` | Retorna os detalhes de um livro.     | -                                                                                                   |
| `POST`   | `/books/`      | Adiciona um novo livro.              | `{ "title": "1984", "author": "George Orwell", "release_year": 1949, "isbn": "978-0-452-28423-4" }` |
| `DELETE` | `/books/<id>/` | Remove um livro pelo ID.             | -                                                                                                   |

## ✅ Requisitos Funcionais

- [✅] O sistema deve permitir o cadastro de novos livros com os seguintes campos obrigatórios: título, autor, ano de publicação e ISBN.
- [✅] O sistema deve retornar uma lista de todos os livros cadastrados no banco de dados. A resposta deve incluir os detalhes dos livros.
- [✅] O sistema deve permitir a busca de um livro específico pelo seu ID.
- [✅] O sistema deve permitir a exclusão de um livro específico, utilizando o ID.

## 🔒 Regras de Negócio

- [✅] Não deve ser possível cadastrar dois livros com o mesmo ISBN.

## 📋 Script de Seed

Foi implementado um comando customizado para popular o banco de dados com exemplos de livros.

### 🔧 Como rodar o seed:

```bash
python manage.py seed
```

Este comando adiciona automaticamente alguns livros ao banco de dados caso ele esteja vazio. Se já existirem dados no banco, o comando não realiza alterações.

## 🚧 Melhorias Futuras

- [ ] Implementar paginação para listar livros.
- [ ] Adicionar autenticação para proteger endpoints sensíveis.
- [ ] Criar testes unitários para todos os endpoints e regras de negócio.
