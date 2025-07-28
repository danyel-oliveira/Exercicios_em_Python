#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
EXERCÍCIO 01 - PROGRAMAÇÃO EM PYTHON
=============================================================================

Descrição: Exercícios básicos de Python envolvendo estruturas condicionais,
           loops, funções e manipulação de dados.

Autor: Danyel Oliveira
Data: 2024
Curso: Análise e Desenvolvimento de Sistemas - 3º Semestre
=============================================================================
"""

# ===== IMPORTS =====
import os
from datetime import datetime


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho():
    """Exibe o cabeçalho do programa."""
    print("=" * 60)
    print("          EXERCÍCIOS EM PYTHON - EXERCÍCIO 01")
    print("=" * 60)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("Autor: Danyel Oliveira")
    print("=" * 60)


# ===== EXERCÍCIO 1: CALCULADORA BÁSICA =====
def calculadora_basica():
    """
    Calculadora que realiza operações básicas entre dois números.
    """
    print("\n🧮 CALCULADORA BÁSICA")
    print("-" * 30)
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == '+':
            resultado = num1 + num2
            print(f"✅ Resultado: {num1} + {num2} = {resultado}")
        elif operacao == '-':
            resultado = num1 - num2
            print(f"✅ Resultado: {num1} - {num2} = {resultado}")
        elif operacao == '*':
            resultado = num1 * num2
            print(f"✅ Resultado: {num1} × {num2} = {resultado}")
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
                print(f"✅ Resultado: {num1} ÷ {num2} = {resultado:.2f}")
            else:
                print("❌ Erro: Divisão por zero não é permitida!")
        else:
            print("❌ Operação inválida! Use apenas +, -, * ou /")
            
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números válidos!")


# ===== EXERCÍCIO 2: VERIFICADOR DE IDADE =====
def verificar_idade():
    """
    Verifica a faixa etária baseada na idade fornecida.
    """
    print("\n👶 VERIFICADOR DE FAIXA ETÁRIA")
    print("-" * 35)
    
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0:
            print("❌ Idade inválida!")
        elif idade <= 12:
            print(f"👶 Com {idade} anos, você é uma CRIANÇA")
        elif idade <= 17:
            print(f"🧒 Com {idade} anos, você é um ADOLESCENTE")
        elif idade <= 59:
            print(f"👨 Com {idade} anos, você é um ADULTO")
        else:
            print(f"👴 Com {idade} anos, você é um IDOSO")
            
    except ValueError:
        print("❌ Erro: Por favor, digite uma idade válida!")


# ===== EXERCÍCIO 3: TABUADA =====
def gerar_tabuada():
    """
    Gera a tabuada de um número escolhido pelo usuário.
    """
    print("\n📊 GERADOR DE TABUADA")
    print("-" * 25)
    
    try:
        numero = int(input("Digite o número para gerar a tabuada: "))
        print(f"\n📋 Tabuada do {numero}:")
        print("-" * 20)
        
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} × {i:2} = {resultado:3}")
            
    except ValueError:
        print("❌ Erro: Por favor, digite um número válido!")


# ===== EXERCÍCIO 4: CONTADOR DE NÚMEROS PARES =====
def contar_pares():
    """
    Conta quantos números pares existem em um intervalo.
    """
    print("\n🔢 CONTADOR DE NÚMEROS PARES")
    print("-" * 32)
    
    try:
        inicio = int(input("Digite o número inicial: "))
        fim = int(input("Digite o número final: "))
        
        if inicio > fim:
            inicio, fim = fim, inicio  # Troca os valores
            
        pares = []
        for num in range(inicio, fim + 1):
            if num % 2 == 0:
                pares.append(num)
        
        print(f"\n📊 Números pares entre {inicio} e {fim}:")
        print(f"🔢 Números: {pares}")
        print(f"📈 Total de números pares: {len(pares)}")
        
    except ValueError:
        print("❌ Erro: Por favor, digite números válidos!")


# ===== EXERCÍCIO 5: LISTA DE NOMES =====
def gerenciar_lista_nomes():
    """
    Permite adicionar e exibir nomes em uma lista.
    """
    print("\n📝 GERENCIADOR DE LISTA DE NOMES")
    print("-" * 35)
    
    nomes = []
    
    while True:
        print(f"\n📋 Lista atual: {nomes}")
        print("\nOpções:")
        print("1 - Adicionar nome")
        print("2 - Remover nome")
        print("3 - Exibir lista completa")
        print("4 - Sair")
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                nome = input("Digite o nome: ").strip().title()
                if nome and nome not in nomes:
                    nomes.append(nome)
                    print(f"✅ '{nome}' adicionado com sucesso!")
                elif nome in nomes:
                    print(f"⚠️  '{nome}' já existe na lista!")
                else:
                    print("❌ Nome inválido!")
                    
            elif opcao == '2':
                if nomes:
                    nome = input("Digite o nome para remover: ").strip().title()
                    if nome in nomes:
                        nomes.remove(nome)
                        print(f"✅ '{nome}' removido com sucesso!")
                    else:
                        print(f"❌ '{nome}' não encontrado na lista!")
                else:
                    print("📭 Lista está vazia!")
                    
            elif opcao == '3':
                if nomes:
                    print(f"\n📋 Lista completa ({len(nomes)} nomes):")
                    for i, nome in enumerate(sorted(nomes), 1):
                        print(f"{i:2}. {nome}")
                else:
                    print("📭 Lista está vazia!")
                    
            elif opcao == '4':
                print("👋 Saindo do gerenciador de nomes...")
                break
                
            else:
                print("❌ Opção inválida! Escolha entre 1-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            break


# ===== MENU PRINCIPAL =====
def menu_principal():
    """
    Exibe o menu principal com todas as opções de exercícios.
    """
    exercicios = {
        '1': ('🧮 Calculadora Básica', calculadora_basica),
        '2': ('👶 Verificador de Idade', verificar_idade),
        '3': ('📊 Gerador de Tabuada', gerar_tabuada),
        '4': ('🔢 Contador de Pares', contar_pares),
        '5': ('📝 Lista de Nomes', gerenciar_lista_nomes),
    }
    
    while True:
        limpar_tela()
        exibir_cabecalho()
        
        print("\n🎯 ESCOLHA UM EXERCÍCIO:")
        print("-" * 30)
        
        for opcao, (titulo, _) in exercicios.items():
            print(f"{opcao} - {titulo}")
        print("0 - 🚪 Sair do programa")
        
        try:
            escolha = input("\n➡️  Digite sua escolha: ").strip()
            
            if escolha == '0':
                print("\n👋 Obrigado por usar o programa!")
                print("🎓 Continue estudando Python!")
                break
                
            elif escolha in exercicios:
                limpar_tela()
                exibir_cabecalho()
                _, funcao = exercicios[escolha]
                funcao()
                input("\n⏸️  Pressione ENTER para continuar...")
                
            else:
                print("❌ Opção inválida! Tente novamente.")
                input("⏸️  Pressione ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            print("🎓 Continue estudando Python!")
            break


# ===== EXECUÇÃO PRINCIPAL =====
if __name__ == "__main__":
    """
    Ponto de entrada principal do programa.
    """
    try:
        menu_principal()
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🔧 Contacte o desenvolvedor se o problema persistir.")
    
    print("\n" + "=" * 60)
    print("           PROGRAMA FINALIZADO")
    print("=" * 60)
