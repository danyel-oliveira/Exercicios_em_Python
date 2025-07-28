{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNEeC0b0B5Hn3akj9XBTvxX",
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
        "<a href=\"https://colab.research.google.com/github/danyel-oliveira/Exercicios_em_Python/blob/main/Lista01_python_basico_ADS_danyel.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1. Escreva um programa que apresente na tela a frase: \"Meu primeiro programa!!!\"\n",
        "print(\"Meu primeiro programa :D !!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GzXRe1ZNKTKX",
        "outputId": "cdc87431-313d-4dde-c3c5-87162e0dce50"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Meu primeiro programa :D !!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#2. Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela o número informado pelo usuário do programa\n",
        "num_inteiro=int(input(\"Digite um número inteiro:\"))\n",
        "print(f\"foi informado o valor:\", num_inteiro)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iW39KFMwLHF2",
        "outputId": "f1e2f342-17e2-4e41-c019-063bdf63e463"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro:234\n",
            "foi informado o valor: 234\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#3. Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela o número informado da seguinte forma: \"Foi informado o valor: X\"\n",
        "\n",
        "num_inteiro = int(input(\"Digite um número inteiro:\"))\n",
        "print(\"Foi informado o valor:\", num_inteiro)"
      ],
      "metadata": {
        "id": "Z1qDYRVmLQGx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5d84077f-56f8-4a61-d9a6-af9cdb45a633"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro:234\n",
            "Foi informado o valor: 234\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#4Escreva um programa que solicite ao usuário dois números inteiros e ao final\n",
        "# apresente na tela os dois números informados da seguinte forma: \"Voce informou os numeros X e Y\"\n",
        "numerInteiro1 = int(input(\"Digite um número inteiro:\"))\n",
        "numerInteiro2 = int(input(\"Digite um número inteiro:\"))\n",
        "print(\"Voce informou os numeros\", numerInteiro1, \"e\", numerInteiro2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HeJmBlvDZubL",
        "outputId": "18a4b843-8c51-460b-975f-44d73b6d3b91"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro:23\n",
            "Digite um número inteiro:37\n",
            "Voce informou os numeros 23 e 37\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#5. Escreva um programa que solicite ao usuário um número real e ao final apresente na tela o número informado formatado com duas casas decimais da seguinte forma: \"Voce informouo numero X.YY\"\n",
        "numerInteiro1 = float(input(\"Digite um número inteiro:\"))\n",
        "print(\"Voce informouo numero\", numerInteiro1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZH45OVtlaORG",
        "outputId": "35cc4fe7-3a1e-405b-a6ea-5770fd31d1bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro:25\n",
            "Voce informouo numero 25.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#6. Escreva um programa que solicite ao usuário a temperatura em graus Celsius e\n",
        "#ao final apresente a temperatura correspondente em graus Farenheit.\n",
        "#F = Celsius * 1.8 + 32\n",
        "Celsius = float(input('Digite a temperatura em Celsus: '))\n",
        "print('A temperatura em Farenheit é:', Celsius * 1.8 + 32)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5eURZxZ3byrr",
        "outputId": "52028a07-bcfe-4b66-a5dc-a4678e5ec8fc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a temperatura em Celsus: 29\n",
            "A temperatura em Farenheit é: 84.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#7.Escreva um programa que solicite ao usuário um número inteiro e um número\n",
        "#real e ao final apresente na tela os dois números informados formatando com\n",
        "#duas casas decimais somente o número real da seguinte forma: \"Voce informou os numeros N e X.YY\"\n",
        "numerInteiro =int (input('Digite um número inteiro: '))\n",
        "numerReal = float(input('Digite um número real: '))\n",
        "print('Voce informou os numeros', numerInteiro, 'e', numerReal)"
      ],
      "metadata": {
        "id": "prqcxNKSdZ4l",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fec0ad84-b5f5-4b2b-c8a9-7626f56a7f85"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro: 5\n",
            "Digite um número real: 24\n",
            "Voce informou os numeros 5 e 24.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#8. Escreva um programa que solicite ao usuário a primeira letra de seu nome e ao final\n",
        "#apresente na tela a letra informada pelo usuário da seguinte forma: \"Voce digitou w\"\n",
        "letra= str(input(\"Digite a primeira letra do seu nome: \"))\n",
        "print (\"Voce digitou\", letra)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eIGXf8uIeTMn",
        "outputId": "143624ed-5bc1-42db-9974-f48cc196b1c7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a primeira letra do seu nome: D\n",
            "Voce digitou D\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#9. Escreva um programa que solicite ao usuário o nome de sua cor preferida e ao final\n",
        "#apresente na tela a cor informada pelo usuário da seguinte forma: \"Voce gosta da cor AAA\"\n",
        "corFavorita = (input('Qual a sua cor favorita?'))\n",
        "print ('Voce gosta da cor', corFavorita)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GzBt-1eoetWx",
        "outputId": "3b59fa9f-a0ee-49aa-c5e5-3e426be62609"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual a sua cor favorita?azul\n",
            "Voce gosta da cor azul\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " #10Escreva um programa que solicite ao usuário o nome de uma verdura e uma fruta de sua preferencia e ao final apresente na tela as informações digitadas pelo usuário da seguinte\n",
        " #forma: \"Voce gosta de AAAAAAA e BBBBBBB\"\n",
        " verdura=str(input(\"Olá digite sua verdura preferida:\"))\n",
        " fruta=str(input(\"Olá digite sua fruta preferida:\"))\n",
        " print(f\"Você gosta de {verdura} e {fruta}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4WUTb5Y0jU_u",
        "outputId": "e053d6d4-d78a-467d-c660-9141ee7ee6a4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá digite sua verdura preferida:batata\n",
            "Olá digite sua fruta preferida:manga\n",
            "Você gosta de batata e manga\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#11. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela o numero informado e na linha de baixo o dobro deste número da seguinte forma:\n",
        "#Numero -> X\n",
        "#Dobro deste numero -> Y\n",
        "num=float(input(\"Digite um número real:\"))\n",
        "print(f\"Número {num}, o dobro de {num} é {num*2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8AfZDBfqmGTd",
        "outputId": "1aea98e6-9a73-4800-ba2e-72447f763ac0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número real:10\n",
            "Número 10.0, o dobro de 10.0 é 20.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#12.Reescrever o programa anterior apresentando o quadrado e o cubo do número informado.\n",
        "num=float(input(\"Informe um número real: \"))\n",
        "print(f\"Número {num}, o quadrado de {num} é {num**2} e o cubo é {num**3}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gCKk-NS-nY60",
        "outputId": "05dae1d2-e836-4589-c202-2d02463db2c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Informe um número real: 20\n",
            "Número 20.0, o quadrado de 20.0 é 400.0 e o cubo é 8000.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#13. Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente\n",
        "#na tela a soma dos dois números informados da seguinte forma: \"O numeros N e X\n",
        "#somados correspondem a Y\"\n",
        "num1=int(input(\"Informe um número inteiro: \"))\n",
        "num2=int(input(\"Informe o segundo número inteiro: \"))\n",
        "resultado= num1+num2\n",
        "print(f\"O número {num1} e {num2} somados corresponde a {resultado}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J345zttopVja",
        "outputId": "110ccf29-79a3-4f09-9be5-bf7395eb46ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Informe um número inteiro: 30\n",
            "Informe o segundo número inteiro: 50\n",
            "O número 30 e 50 somados corresponde a 80\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#14. Escreva um programa que solicite ao usuário dois números reais e ao final apresente na\n",
        "#tela o produto dos dois números informados da seguinte forma: \"O produto dos numeros N\n",
        "#e X corresponde a Y\"\n",
        "num1=float(input(\"Informe um número real: \"))\n",
        "num2=float(input(\"Informe o segundo número real: \"))\n",
        "resultado= num1+num2\n",
        "print(f\"O produto dos números {num1} e {num2} corresponde a {resultado}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hRBgjp-6piWk",
        "outputId": "dcdba7d4-9442-4c11-ea37-aa7cef7efc53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Informe um número real: 71\n",
            "Informe o segundo número real: 3560\n",
            "O produto dos números 71.0 e 3560.0 corresponde a 3631.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#15. Refazer o programa 14 realizando as quatro operações aritméticas básicas\n",
        "num1=float(input(\"Informe um número real: \"))\n",
        "num2=float(input(\"Informe o segundo número real: \"))\n",
        "print(f\"O produto dos números {num1} e {num2} corresponde a {num1+num2}\")\n",
        "print(f\"O produto dos números {num1} e {num2} corresponde a {num1-num2}\")\n",
        "print(f\"O produto dos números {num1} e {num2} corresponde a {num1*num2}\")\n",
        "print(f\"O produto dos números {num1} e {num2} corresponde a {num1/num2}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QtWFBNG0sX0s",
        "outputId": "c017a787-c4c2-4c48-cdb3-b3437ba51132"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Informe um número real: 35\n",
            "Informe o segundo número real: 25\n",
            "O produto dos números 35.0 e 25.0 corresponde a 60.0\n",
            "O produto dos números 35.0 e 25.0 corresponde a 10.0\n",
            "O produto dos números 35.0 e 25.0 corresponde a 875.0\n",
            "O produto dos números 35.0 e 25.0 corresponde a 1.4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#16.Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendido no mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.\n",
        "salario_fixo = float(input(\"Digite o salário fixo do vendedor: \"))\n",
        "total_vendido = float(input(\"Digite o total vendido no mês: \"))\n",
        "percentual_comissao = float(input(\"Digite o percentual de comissão (em %): \"))\n",
        "comissao = (percentual_comissao / 100) * total_vendido\n",
        "salario_bruto = salario_fixo + comissao\n",
        "print(f\"O salário bruto do vendedor é: R$ {salario_bruto:.2f}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-SQMdH7AuKFS",
        "outputId": "43c59c4d-a14c-4449-ef58-485615eccfc6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o salário fixo do vendedor: 1560\n",
            "Digite o total vendido no mês: 2500\n",
            "Digite o percentual de comissão (em %): 5\n",
            "O salário bruto do vendedor é: R$ 1685.00\n"
          ]
        }
      ]
    }
  ]
}