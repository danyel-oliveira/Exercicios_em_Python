{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMSNcDOYw/+5TLJc1aOPHTu",
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
        "<a href=\"https://colab.research.google.com/github/danyel-oliveira/Exercicios_em_Python/blob/main/exercicio_01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "Vl-h2AiVyiC5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#criando uma classe\n",
        "class Usuario:\n",
        "    def __init__(self, nome, idade, curso, rotina, objetivo):\n",
        "        self.nome = nome\n",
        "        self.idade = idade\n",
        "        self.curso = curso\n",
        "        self.rotina = rotina\n",
        "        self.objetivo = objetivo\n",
        "\n",
        "    def estudar(self):\n",
        "        return f\"{self.nome} está estudando {self.curso} e tem {len(self.rotina['materias'])} matérias na faculdade.\"\n",
        "\n",
        "    def trabalhar(self):\n",
        "        return f\"{self.nome} trabalha como freelancer e está sempre buscando novos projetos.\"\n",
        "\n",
        "    def treinar(self):\n",
        "        return f\"{self.nome} faz musculação dia sim, dia não para manter a saúde.\"\n",
        "\n",
        "    def lazer(self):\n",
        "        return f\"{self.nome} tira um tempo para relaxar e explorar assuntos de interesse como filosofia e tecnologia.\"\n",
        "\n",
        "    def objetivo_de_vida(self):\n",
        "        return f\"O grande objetivo de {self.nome} é {self.objetivo}.\"\n",
        "\n",
        "# Criando um objeto com suas informações\n",
        "usuario = Usuario(\n",
        "    nome=\"Usuário\",\n",
        "    idade=25,  # Exemplo de idade\n",
        "    curso=\"Análise e Desenvolvimento de Sistemas\",\n",
        "    rotina={\n",
        "        \"materias\": [\"Banco de Dados\", \"Programação\", \"Engenharia de Software\", \"Redes\"],\n",
        "        \"trabalho\": \"Freelancer\",\n",
        "        \"atividade_fisica\": \"Musculação dia sim, dia não\"\n",
        "    },\n",
        "    objetivo=\"ser empreendedor na área de TI\"\n",
        ")\n",
        "\n",
        "# Chamando métodos para exibir informações\n",
        "print(usuario.estudar())\n",
        "print(usuario.trabalhar())\n",
        "print(usuario.treinar())\n",
        "print(usuario.lazer())\n",
        "print(usuario.objetivo_de_vida())\n"
      ],
      "metadata": {
        "id": "XGUgZo8jynKK",
        "outputId": "c9f39b4a-ed6b-4d79-c721-d4a83959f1ae",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usuário está estudando Análise e Desenvolvimento de Sistemas e tem 4 matérias na faculdade.\n",
            "Usuário trabalha como freelancer e está sempre buscando novos projetos.\n",
            "Usuário faz musculação dia sim, dia não para manter a saúde.\n",
            "Usuário tira um tempo para relaxar e explorar assuntos de interesse como filosofia e tecnologia.\n",
            "O grande objetivo de Usuário é ser empreendedor na área de TI.\n"
          ]
        }
      ]
    }
  ]
}