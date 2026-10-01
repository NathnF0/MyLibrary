# 📚 MyLibrary // Personal Library System

O **MyLibrary** é uma aplicação web para gerenciamento de biblioteca pessoal, desenvolvida em Python com Flask. O sistema permite organizar livros, acompanhar o status de leitura e visualizar o progresso da biblioteca através de uma interface limpa, responsiva e com suporte a tema claro e escuro.

## 🚀 Evolução do Projeto

O projeto foi desenvolvido com foco em transformar uma necessidade simples — organizar livros e leituras — em uma aplicação web completa.

A versão **1.0** conta com persistência de dados, gerenciamento completo dos livros, sistema de progresso, níveis de leitura e conquistas, mantendo uma arquitetura simples e funcional.

## 🛠️ Tech Stack

- **Backend:** Python 3.12+
- **Web Framework:** Flask
- **Database:** SQLite
- **ORM:** Flask-SQLAlchemy
- **Frontend:** HTML5 + CSS3
- **Temas:** Light Mode / Dark Mode
- **Templates:** Jinja2

## 💎 Funcionalidades

- **Library Management:** Cadastro, edição e exclusão de livros.
- **Reading Status:** Organização por "Pretendo Ler", "Lendo" e "Concluído".
- **Reading Dashboard:** Visualização rápida do total de livros, leituras em andamento e concluídas.
- **Level System:** Sistema de níveis baseado na quantidade de livros cadastrados.
- **Achievements:** Conquistas desbloqueadas conforme a evolução da biblioteca.
- **Theme System:** Alternância entre tema claro e escuro com persistência da preferência.
- **Persistent Data:** Armazenamento local utilizando SQLite.
- **Responsive Interface:** Interface adaptada para diferentes tamanhos de tela.

## 📦 Como Rodar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/NathnF0/MyLibrary.git
   cd MyLibrary

2. Crie o ambiente virtual:
   python -m venv venv
3. Ative o ambiente virtual:
   Windows:
   venv\Scripts\activate
4. Instale as dependências:
   pip install flask flask-sqlalchemy
5. Inicie a aplicação:
   python app.py
6. Acesse no navegador:
   http://127.0.0.1:5000
🗂️ Estrutura do Projeto
MyLibrary/
├── app.py
├── templates/
│   ├── index.html
│   ├── add_book.html
│   ├── edit_book.html
│   └── profile.html
├── static/
│   ├── style.css
│   └── theme.js
├── instance/
│   └── mylibrary.db
└── .gitignore

O banco SQLite é criado localmente e não é versionado pelo Git.

## 👨‍💻 Developer

**NATHNF**  
*Systems Developer*

Desenvolvedor focado em Python, aplicações web e integração entre backend e interfaces funcionais.

**Core Stack:** Flask · SQLite · SQLAlchemy · HTML · CSS · JavaScript

**Focus:** Clean Code · Data Organization · UI/UX

> *"Organize your books. Track your journey."*
