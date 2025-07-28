{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNeuc/0ajVaE1Oe73S8kSMH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/danyel-oliveira/Exercicios_em_Python/blob/main/Exerc%C3%ADcioSQLite_POO_Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5cns32Qkwcow",
        "outputId": "48290e54-d366-4f97-a287-a59fd48903d1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Coneção estabelecida com banco de dandos: meu_banco_de_dados.db\n",
            "Tabela 'clientes' criada com sucesso.\n",
            "Dados inseridos na tabela 'clientes' com sucesso\n",
            "\n",
            "Todos os clientes:\n",
            "(1, 'Ricardo Silva', 'Ricardo.silva@email.com', 35)\n",
            "(2, 'Maria Santos', 'Maria.santos@email.com', 28)\n",
            "(3, 'Carlos Alberto', 'carlos.alberto@email.com', 42)\n",
            "(4, 'Ana Oliveira', 'ana.oliveira@email.com', 31)\n",
            "(5, 'Pedro Souza', 'pedro.souza@email.com', 29)\n",
            "(6, 'Julia Ferreira', 'julia.ferreira@email.com', 37)\n",
            "(7, 'Lucas Martins', 'lucas.martins@email.com', 26)\n",
            "\n",
            "Clientes com mais de 30 anos (apenas nome e email):\n",
            "('Ricardo Silva', 'Ricardo.silva@email.com')\n",
            "('Carlos Alberto', 'carlos.alberto@email.com')\n",
            "('Ana Oliveira', 'ana.oliveira@email.com')\n",
            "('Julia Ferreira', 'julia.ferreira@email.com')\n",
            "\n",
            "Conexão com o banco de dados fechada.\n"
          ]
        }
      ],
      "source": [
        "import sqlite3\n",
        "\n",
        "#Especifique o nome do arquevo do banco de danos.\n",
        "#Se o arquivo 'meu_banco_de_dados.db' não existir, ele sera criado.\n",
        "nome_do_banco = \"meu_banco_de_dados.db\"\n",
        "\n",
        "#Tentar conectar ao banco de danos.\n",
        "conexao = sqlite3.connect(nome_do_banco)\n",
        "\n",
        "#Crie um cursor. O cursor permite executar comandos SQL.\n",
        "cursor = conexao.cursor()\n",
        "\n",
        "print(f\"Coneção estabelecida com banco de dandos: {nome_do_banco}\")\n",
        "\n",
        "#Comando SQL para criar a tabela 'clientes' se ela não existir.\n",
        "comando_criar_tabela = \"\"\"\n",
        "CREATE TABLE IF NOT EXISTS clientes (\n",
        "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "  nome TEXT NOT NULL,\n",
        "  email TEXT UNIQUE,\n",
        "  idade INTEGER\n",
        ")\n",
        "\"\"\"\n",
        "\n",
        "#Execute o comando SQL usando o cursor.\n",
        "cursor.execute(comando_criar_tabela)\n",
        "\n",
        "#Commit as alterações. Isso salva a criação da tabela no banco de dados.\n",
        "conexao.commit()\n",
        "\n",
        "print(\"Tabela 'clientes' criada com sucesso.\")\n",
        "\n",
        "comando_inserir_dados = \"\"\"\n",
        "INSERT INTO clientes (nome, email, idade) VALUES (?, ?, ?)\n",
        "\"\"\"\n",
        "\n",
        "#Dados para inserir na tabela.\n",
        "dados_cliente1 = ('Ricardo Silva', 'Ricardo.silva@email.com', 35)\n",
        "cursor.execute(comando_inserir_dados, dados_cliente1)\n",
        "\n",
        "#Dados do segundo cliente\n",
        "dados_cliente2 = ('Maria Santos', 'Maria.santos@email.com', 28)\n",
        "cursor.execute(comando_inserir_dados, dados_cliente2)\n",
        "\n",
        "# Você tambem pode inserir vários registros de uma vez usando 'executemany()'.\n",
        "lista_de_clientes = [\n",
        "    ('Carlos Alberto', 'carlos.alberto@email.com', 42),\n",
        "    ('Ana Oliveira', 'ana.oliveira@email.com', 31),\n",
        "    ('Pedro Souza', 'pedro.souza@email.com', 29),\n",
        "    ('Julia Ferreira', 'julia.ferreira@email.com', 37),\n",
        "    ('Lucas Martins', 'lucas.martins@email.com', 26)\n",
        "]\n",
        "\n",
        "cursor.executemany(comando_inserir_dados, lista_de_clientes)\n",
        "\n",
        "#Commit as alterações para salvar os dados no banco de dados.\n",
        "conexao.commit()\n",
        "\n",
        "print(\"Dados inseridos na tabela 'clientes' com sucesso\")\n",
        "\n",
        "comando_selecionar_todos = \"\"\"\n",
        "SELECT * FROM clientes\n",
        "\"\"\"\n",
        "\n",
        "#Execute o comando SQL\n",
        "cursor.execute(comando_selecionar_todos)\n",
        "\n",
        "#Recupere todos os resultados da consulta.\n",
        "resultados = cursor.fetchall()\n",
        "\n",
        "#Intere sobre os resultados e imprima cada linha.\n",
        "print(\"\\nTodos os clientes:\")\n",
        "for linha in resultados:\n",
        "    print(linha)\n",
        "\n",
        "#Você tambem pode selecionar colunas especificas e usar a clausula 'WHERE' para filtrar os resultados.\n",
        "comando_selecionar_nomes_emails = \"\"\"\n",
        "SELECT nome, email FROM clientes WHERE idade > ?\n",
        "\"\"\"\n",
        "\n",
        "cursor.execute(comando_selecionar_nomes_emails, (30,))\n",
        "resultados_filtrados = cursor.fetchall()\n",
        "\n",
        "print(\"\\nClientes com mais de 30 anos (apenas nome e email):\")\n",
        "for linha in resultados_filtrados:\n",
        "    print(linha)\n",
        "\n",
        "conexao.close()\n",
        "\n",
        "print(\"\\nConexão com o banco de dados fechada.\")"
      ]
    }
  ]
}