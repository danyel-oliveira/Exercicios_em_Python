{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP92oJD+QvzWsfGexLH450V",
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
        "<a href=\"https://colab.research.google.com/github/danyel-oliveira/Exercicios_em_Python/blob/main/exercicio_02.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "source": [
        "#1- Elabore um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que 10 (dez)\n",
        "num= float(input(\"Informe um número: \"))\n",
        "if num >= 10:\n",
        "    print(f\"O número {num} é maior que 10\")"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "euzFnvkrzU5n",
        "outputId": "825b2ddb-d36e-4a91-842e-b5d7660b68c4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Informe um número: 20\n",
            "O número 20.0 é maior que 10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#2- Escreva um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior ou igual a dez oumenor que 10 (dez)\n",
        "num1= float(input(\"Olá, digite um número real:\"))\n",
        "if num1 >= 10:\n",
        "  print(f\"O número {num1} é maior ou igual a 10\")\n",
        "else:\n",
        "   print(f\"O número {num1} é menor que 10\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FIzCVJnrzlxH",
        "outputId": "aac5e349-7965-40fa-fdc4-f7019d223a7b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número real:5\n",
            "O número 5.0 é menor que 10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#3- Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que dez, se é menor que dez, ou se é igual a dez.\n",
        "num1= float(input(\"Olá, digite um número real: \"))\n",
        "if num1>10:\n",
        "    print(f\"O número {num1} é maior que 10\")\n",
        "if num1==10:\n",
        "    print(f\"O número {num1} é igual a 10\")\n",
        "if num1<10:\n",
        "    print(f\"O número {num1} é menor que 10\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oGuYdq4E0gW2",
        "outputId": "4bfa030b-a19e-4dba-c96b-563b9323cf5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número real: 88\n",
            "O número 88.0 é maior que 10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#4- Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é positivo, negativo ou nulo (zero)\n",
        "num1= float(input(\"Olá, digite um número real: \"))\n",
        "if num1>0:\n",
        "    print(f\"O número {num1} é positivo\")\n",
        "elif num1==0:\n",
        "    print(\"Número nulo\")\n",
        "else:\n",
        "    print(f\"O número {num1} é negativo \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jzbra6YC3Wqi",
        "outputId": "cb66bfaa-0716-4564-ea51-89859047792c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número real: 5\n",
            "O número 5.0 é positivo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "zzLe_wwWAUSs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#5- Elabore um algoritmo que leia um número inteiro e imprima uma das mensagens: é múltiplo de 3, ou, não é múltiplo de 3\n",
        "num1= int (input(\"Olá, digite um número inteiro: \"))\n",
        "if num1 % 3==0:\n",
        "  print (f\"{num1} é multiplo de 3\")\n",
        "else:\n",
        "  print(f\"{num1} não é multiplo de 3\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0ZeYsut23_Xg",
        "outputId": "94d835e3-ede4-4d41-a6c2-349c94a785c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número inteiro: 5\n",
            "5 não é multiplo de 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#6- Refazer o exercício anterior, solicitando antes o múltiplo a ser testado\n",
        "num= int(input(\"Olá, digite um número inteiro: \"))\n",
        "mult= int(input(\"Digite o multiplo desejado: \"))\n",
        "if num % mult==0:\n",
        "    print(f\"{num} é multiplo de {mult}\")\n",
        "else:\n",
        "    print(f\"{num} não é multiplo de {mult}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xp6R9doF4sRl",
        "outputId": "f8f1c2f5-1bfe-4b71-e72b-9d7698b22dd1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número inteiro: 89\n",
            "Digite o multiplo desejado: 9\n",
            "89 não é multiplo de 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#7Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como par ou ímpar.\n",
        "num= int(input(\"Olá, digite um número inteiro: \"))\n",
        "if num % 2==0:\n",
        "    print(f\"{num} é par\")\n",
        "else:\n",
        "    print(f\"{num} é ímpar\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K3Y0uiZO5Ilr",
        "outputId": "3effbc70-c23f-42e9-a182-0bd1ceb26d05"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número inteiro: 250\n",
            "250 é par\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#8- Elabore um algoritmo que leia um número, e se ele for maior do que 20, imprimir a metade desse número, caso contrário, imprimir o dobro do número.\n",
        "num= float(input(\"Olá, digite um número: \"))\n",
        "if num>20:\n",
        "    print(f\"A metade de {num} é {num/2}\")\n",
        "else:\n",
        "    print(f\"O dobro de {num} é {num*2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sQPHCQhk6rfQ",
        "outputId": "9f6a3f79-d0d7-478b-f5e5-5c203a01e36d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número: 300\n",
            "A metade de 300.0 é 150.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#9- Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele.\n",
        "num= int(input(\"Olá, digite um número inteiro: \"))\n",
        "num1= int(input(\"Olá, digite outro número inteiro: \"))\n",
        "resultado=num+num1\n",
        "if resultado>10:\n",
        "    print(f\"O número {num} somado a {num1} ao quadrado é {resultado**2}\")\n",
        "else:\n",
        "    print(f\"O número {num} somado a {num1} a metade do resultado é 6{resultado/2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "odJ_8piX7IDq",
        "outputId": "347b50d1-e39d-4b88-dc0e-c1dea3077ed3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número inteiro: 5\n",
            "Olá, digite outro número inteiro: 8\n",
            "O número 5 somado a 8 ao quadrado é 169\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#10- O sistema de avaliação de determinada disciplina é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 3 e a\n",
        "#terceira tem peso 5. Considerando que a média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno desta\n",
        "#disciplina e dizer se o aluno foi aprovado ou não.\n",
        "\n",
        "nota1= float(input(\"Olá, informe a primeira nota: \"))\n",
        "nota2= float(input(\"Informe a segunda nota: \"))\n",
        "nota3= float(input(\"Informe a terceira nota: \"))\n",
        "media=(nota1+nota2+nota3)/ 3\n",
        "if media>=6:\n",
        "    print (\"Sua média é: \", media,\"! APROVADO!!!!!!\")\n",
        "else:\n",
        "    print (\"Sua média é: %.2f\" % media ,\"! Reprovado\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n71olNOr7kz8",
        "outputId": "18cc3eff-f59f-435d-e8fd-bd46180457e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, informe a primeira nota: 85\n",
            "Informe a segunda nota: 10\n",
            "Informe a terceira nota: 95\n",
            "Sua média é:  63.333333333333336 ! APROVADO!!!!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#11- Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da pessoa mais pesada.\n",
        "nome1= str(input(\"Por gentileza informe o nome: \"))\n",
        "peso1= float (input(\"Por gentileza informe o peso: \"))\n",
        "nome2= str(input(\"Por gentileza informe o nome da segunda pessoa: \"))\n",
        "peso2= float(input(\"Por gentileza informe o peso da segunda pessoa: \"))\n",
        "if peso1>peso2:\n",
        "    print(f\"{nome1} é mais pesado!\")\n",
        "else:\n",
        "    print(f\"{nome2} é mais pesado!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yuEqXkWl8hJG",
        "outputId": "4fdd6bbe-7e2f-4f63-f729-414bb91a1df5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Por gentileza informe o nome: danyel\n",
            "Por gentileza informe o peso: 78\n",
            "Por gentileza informe o nome da segunda pessoa: izabelle\n",
            "Por gentileza informe o peso da segunda pessoa: 62\n",
            "danyel é mais pesado!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#12. Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e 90, ou não.\n",
        "num= float(input(\"Olá, digite um número: \"))\n",
        "if num>=20 and num<=90:\n",
        "  print(f\"O número {num} encontra-se entre 20 e 90\")\n",
        "else:\n",
        "  print(f\"O número {num} **não** encontra-se entre 20 e 90\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-WV17O7S-0uI",
        "outputId": "7dd8e573-d28c-458a-d73b-1b474b114f6b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite um número: 85\n",
            "O número 85.0 encontra-se entre 20 e 90\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#13.Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se são iguais.\n",
        "num1= float(input(\"Olá, digite o primeiro número: \"))\n",
        "num2= float(input(\"Olá, digite o segundo número: \"))\n",
        "if num1>num2:\n",
        "    print(f\"{num1} é maior o maior número e {num2} é o menor\")\n",
        "elif num1==num2:\n",
        "    print(f\"{num1} é igual a {num2}\")\n",
        "else:\n",
        "    print(f\"{num2} é maior o maior número e {num1} é o menor\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T32iJbYK_LjB",
        "outputId": "290e8e82-a15c-46b7-84f1-b5fec79a6266"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá, digite o primeiro número: 45\n",
            "Olá, digite o segundo número: 35\n",
            "45.0 é maior o maior número e 35.0 é o menor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#14. Escreva um programa em linguagem C que solicite ao usuário a média para aprovação em um curso e em seguida solicite ao usuário o\n",
        "#nome, sexo e as 03 notas do aluno e ao final imprima a frase: \"O aluno XXXXX foi aprovado com media YY\" considerando o gênero do(a)\n",
        "#aluno(a) e se foi aprovado(a) ou reprovado(a).\n",
        "\n",
        "media=float(input(\"Olá! Por gentileza informe a média para aprovação: \"))\n",
        "nome=str(input(\"Informe seu nome: \"))\n",
        "sexo=str(input(\"Informe seu sexo (M/F): \"))\n",
        "nota1=float(input(\"Digite a primeira nota: \"))\n",
        "nota2=float(input(\"Digite a segunda nota: \"))\n",
        "nota3=float(input(\"Digite a terceira nota: \"))\n",
        "media= (nota1+nota2+nota3)/3\n",
        "if smedia>media:\n",
        "    if sexo== \"M\":\n",
        "        print(f\"O aluno {nome} foi aprovado com media {smedia:2f}! Parabéns!\")\n",
        "    elif sexo== \"F\":\n",
        "        print(f\"A aluna {nome} foi aprovada com media {smedia:2f}! Parabéns!\")\n",
        "else:\n",
        "    if sexo== \"M\":\n",
        "        print(f\"O aluno {nome} foi reprovado com media {smedia:2f}! Estude mais!\")\n",
        "    elif sexo== \"F\":\n",
        "        print(f\"A aluna {nome} foi reprovada com media {smedia:2f}! Estude mais!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d5wiMSVx_hkE",
        "outputId": "8026f02d-6a1e-4888-aede-545e5c011839"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá! Por gentileza informe a média para aprovação: 6\n",
            "Informe seu nome: danyel\n",
            "Informe seu sexo (M/F): M\n",
            "Digite a primeira nota: 8\n",
            "Digite a segunda nota: 10\n",
            "Digite a terceira nota: 9\n",
            "O aluno danyel foi aprovado com media 9.000000! Parabéns!\n"
          ]
        }
      ]
    }
  ]
}