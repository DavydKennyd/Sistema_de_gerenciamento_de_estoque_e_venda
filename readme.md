# 📦 Sistema de Controle de Estoque e Vendas

Sistema desenvolvido com Django para gerenciamento de estoque, movimentações de produtos e controle de vendas.

## 📌 Funcionalidades até o momento:

- Cadastro de produtos, fornecedores e clientes (via Django Admin)
- Controle de movimentações de estoque:
  - Entradas e saídas de produtos
  - Atualização automática do estoque após cada movimentação
  - Listagem de movimentações realizadas
- Interface web para:
  - Visualizar todas as movimentações de estoque
  - Cadastrar nova movimentação (entrada/saída)


## 📂 Estrutura de Diretórios

```plaintext
estoque_vendas/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── movimentacoes.html
│   │       └── nova_movimentacao.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── estoque_vendas/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```


## Tecnologias e Bibliotecas
- Python 3.12

- Django 5.2.4

- SQLite (banco padrão do Django para testes locais)

## 📦 Instalação e Execução
- Clone o repositório:

```bash

git clone https://github.com/DavydKennyd/Sistema_de_gerenciamento_de_estoque_e_venda.git
cd repositorio_clonado
```
- Crie o ambiente virtual e instale as dependências:

```bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Rode as migrações e o servidor:

```bash

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Acesse: http://127.0.0.1:8000/admin/

## 📄 Licença
 - Este projeto foi desenvolvido para fins acadêmicos e não possui fins comerciais.

 ## Autor
 -  Desenvolvido por [Davyd Kennyd](https://github.com/DavydKennyd)

## Contato
Para sugestões ou colaborações:
- Email: Kennyd3030@gmail.co
- LinkedIn: https://www.linkedin.com/in/davydkennyd
