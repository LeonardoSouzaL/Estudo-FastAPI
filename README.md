# Estudos com FastAPI

Repositório criado para registrar minha evolução no curso de **FastAPI**, passando pelos principais conceitos de criação de APIs, CRUD, integração com banco de dados, autenticação, autorização e deploy em ambiente Linux.

## Objetivo

Este projeto tem como objetivo consolidar os estudos práticos com **FastAPI**, aplicando conceitos fundamentais de desenvolvimento backend moderno com Python, incluindo rotas, validações, banco de dados, autenticação JWT e estruturação de projetos.

## Conteúdos estudados

Durante o curso foram abordados os seguintes tópicos:

* Conceitos essenciais sobre APIs
* Introdução ao FastAPI
* Programação assíncrona
* Métodos HTTP: `GET`, `POST`, `PUT` e `DELETE`
* Path Parameters, Query Parameters e Header Parameters
* Injeção de dependências com `Depends`
* Validações com Pydantic
* CRUD com FastAPI e SQLAlchemy
* CRUD com FastAPI e SQLModel
* Integração com PostgreSQL
* Criação automática de tabelas
* Organização do projeto em módulos
* Autenticação e autorização com JWT
* Login com OAuth2
* Proteção de rotas por usuário autenticado
* Deploy em Cloud Linux com NGINX e PostgreSQL

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy
* SQLModel
* PostgreSQL
* AsyncPG
* JWT
* Passlib / Bcrypt
* NGINX
* Git e GitHub

## Estrutura do repositório

O repositório foi organizado por seções do curso:

```text
Estudo-FastAPI/
│
├── secao02/
├── secao03_p1/
├── secao03_p2/
├── secao04/
├── secao05/
├── secao06/
└── README.md
```

Cada seção representa uma etapa do aprendizado, iniciando pelos conceitos básicos do FastAPI até a implementação de autenticação, autorização e preparação para deploy.

## Principais funcionalidades implementadas

### CRUD de Cursos

Implementação das operações básicas:

* Listar cursos
* Buscar curso por ID
* Criar curso
* Atualizar curso
* Remover curso

### CRUD com Banco de Dados

Integração com PostgreSQL utilizando SQLAlchemy e SQLModel, com criação automática das tabelas e uso de sessões assíncronas.

### Autenticação e Autorização

Implementação de autenticação com JWT, incluindo:

* Cadastro de usuários
* Login
* Geração de token
* Validação de usuário autenticado
* Proteção de rotas
* Relacionamento entre usuários e artigos

### CRUD de Artigos

Implementação de artigos vinculados ao usuário autenticado, com validação de dados e controle de permissão para edição e exclusão.

## Ajustes realizados durante o curso

Como algumas bibliotecas evoluíram em relação à versão usada no curso, foram necessários alguns ajustes, como:

* Troca de `BaseSettings` para o pacote `pydantic-settings`
* Ajuste de `orm_mode` para `from_attributes` no Pydantic v2
* Conversão de campos `HttpUrl` para `str` antes de salvar no PostgreSQL
* Ajustes em versões de pacotes como `bcrypt`
* Correções em rotas, imports e validações

Esses ajustes ajudaram a entender melhor as diferenças entre versões e a resolver problemas reais de compatibilidade em projetos Python.

## Como executar o projeto

Acesse a pasta da seção desejada, por exemplo:

```bash
cd secao06
```

Crie e ative a virtualenv:

```bash
python -m venv venv
```

No Windows:

```bash
.\venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a conexão com o banco de dados no arquivo de configurações ou em um `.env`, conforme a estrutura da seção.

Para criar as tabelas:

```bash
python criar_tabelas.py
```

Para iniciar a API:

```bash
python main.py
```

Ou:

```bash
python -m uvicorn main:app --reload
```

A documentação interativa ficará disponível em:

```text
http://127.0.0.1:8000/docs
```

## Status do projeto

Curso finalizado, com implementação prática dos principais conceitos de FastAPI, CRUD, banco de dados, autenticação e preparação para deploy.

## Observação

Este repositório tem finalidade de estudo e prática. A estrutura e algumas implementações seguem o fluxo do curso, com adaptações feitas para funcionar com versões mais recentes das bibliotecas utilizadas.
