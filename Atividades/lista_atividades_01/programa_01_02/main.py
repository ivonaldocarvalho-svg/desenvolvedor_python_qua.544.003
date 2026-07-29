# TODO: atividade 02
"""
Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A Volta dos Que Não Foram (livre)
- A Roda Quadrada (12 anos)
- As Tranças do Rei Careca (14 anos)
- Poeira em Alto Mar (16 anos)
- A Vingança do Frango Assado (18 anos)
O usuário irá escolher a sala onde o filme desejado etá passando. Caso o usuário não tenha idade, o programa impede sua e re-exibe a lista para que o mesmo possa escolher outro. Caso o usuário tenha a idade mínima, o programa grava em arquivo o bilhete do filme e encerra o programa.
"""

# importa biblioteca
import os

# limpa tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# entrada de dados
nome = input("Digite seu nome").strip()
idade = int(input("Digite sua idade: "))

os.system('cls' if os.name == 'nt' else 'clear')

# inicia loop infinito
while True:
    # exibe as salas e os filmes
    print("\n===== FIMES EM CARTAZ =====")
    print("Sala 1 - A Volta dos Que Não Foram (lIVRE)")
    print("Sala 2 - A Roda Quadrada (12 anos)")
    print("Sala 3 - As Tranças do Rei Careca (14 anos)")
    print("Sala 4 - Poeira em Alto Mar (16 anos)")
    print("Sala 5 - A Vingança do Frango Assado (18 anos)")

    # recebe do usuário a sala desejada
    sala = input("Escolha a sala do filme desejado (1-5): ").strip()

    os.system('cls' if os.name == 'nt' else 'clear')

    # verifica a sala informada, atribui a idade mínima e o filme
    match sala:
        case "1":
            idade_minima = 0
            filme = "A Volta dos Que Não Foram"
        case "2":
            idade_mínima = 12
            filme = "A Roda Quadrada"
        case "3":
            idade_mínima = 14
            filme = "As Tranças do Rei Careca"
        case "4":
            idade_mínima = 16
            filme = "Poeira em Alto Mar"
        case "5":
            idade_mínima = 18
            filme = "A Vingança do Frango Assado"
        case   _:
        # caso a sala informada não exista
         os.system('cls' if os.name == 'nt' else 'clear')
         print("Sala inexistente. Escolha outra sala.")
         continue
        
    # verifica se o usuário tem a idade mínima
    if idade < idade_minima:
        # proibe a entrada do usuário
        print("f{nome}, você não tem idade suficiente para assistir '{filme}'.")
        print("Por favor, escolha outro filme.")

        # reinicia o loop
        continue
        
    else:
        # imprime a mensagem de sucesso
        print("Ingresso comprado com sucesso! Tenha um bom filme!")

        # grava o ingresso em arquivo
    ingresso = f"Ingresso comprado para: {nome}\n filme: {filme}"
    with open("ingresso.txt", "w", encoding="utf-8") as f:
        f.write(ingresso)

    break