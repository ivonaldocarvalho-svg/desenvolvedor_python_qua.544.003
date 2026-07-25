# TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário e informe na tela o seu IMC o seu diagnóstico com base no valor do IMC.
"""
# NOTE: imc = peso/(altura**2)




# declaração de variáveis
nome = input("Informe seu nome: ").title()
peso = input("Informe seu peso: ")
altura = input("Informe sua altura em metros: ").replace(",",".")


# Saída de dados
print(f"Seu nome é {nome}. {type(nome)}")
print(f"Seu peso é {peso}. {type(peso)}")
print(f"Sua altura é {altura} m. {type(altura)}")


