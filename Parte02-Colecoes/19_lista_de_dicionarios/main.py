# lista de dicionários
usuarios = [
    {
        'nome': "Fulano",
        'idade': 18,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cicrano",
        'idade': 21,
        'email': "Cicrano@gmail.com"
    },
    {
        'nome': "Beltrano",
        'idade': 35,
        'email': "Beltrano@gmail.com"
    }
]

# percorre a lista de dicionário
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")