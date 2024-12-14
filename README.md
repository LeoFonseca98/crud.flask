# CRUD SIMPLES COM FLASK

## Descrição
Este projeto é uma aplicação simples de CRUD (Create, Read, Update, Delete) desenvolvida com Flask. A interface possui uma tela inicial com dois botões: um para adicionar um usuário e outro para listar todos os usuários registrados. Na lista de usuários, há dois botões para cada usuário: um para editar e outro para deletar. O sistema permite adicionar, editar e deletar usuários, interagindo diretamente com um banco de dados PostgreSQL.

## Tecnologias Utilizadas
- Python 3
- Flask
- PostgreSQL

## Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone <url-do-repositorio>
    cd <diretorio-do-repositorio>
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o aplicativo:
    ```bash
    python3 app.py
    ```

5. Acesse o projeto em seu navegador:
    ```
    http://127.0.0.1:5000/
    ```

## Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`.
