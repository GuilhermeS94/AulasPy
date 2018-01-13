"""
Tomadas de decisões:
Como? Pergunte!!!
"""


variavel = "Olá, tudo bem com você?"
print(variavel)

if variavel == "Olá, tudo bem com você?":
    print("OOi, tudo bem, e com você?")


variavel = "Olá, boa noite!"
print(variavel)

if variavel == "Olá, tudo bem com você?":
    print("OOi, tudo bem, e com você?")
else:
    print("Boa noite!")


variavel = "Boa tarde, tudo bem?"
print(variavel)

if variavel == "Olá, tudo bem com você?":
    print("OOi, tudo bem, e com você?")
elif variavel == "Boa tarde, tudo bem?":
    print("Boa tarde, tudo sim e com você?")
else:
    print("Boa noite!")


variavel = "Não estou bem!"
print(variavel)

if variavel == "Não estou bem!":
    print("Hmmm está com dor de cabeça?")
elif variavel == "Ai que dor de cabeça...":
    print("Você quer um remédio?")
elif variavel == "Axo que estou com febre":
    print("Vem aqui que eu vou medir sua temperatura")
else:
    print("Tchau!")

opcoes = {
    "Não estou bem!": "Resposta 1",
    "Boa tarde, tudo bem?": "Resposta 2",
    "Olá, tudo bem com você?": "Resposta 3",
    "Olá, boa noite!": "Resposta 4",
    "Não estou afim de papo hoje!": "Resposta 5"
}

print("______________")
print(opcoes[variavel])


variavel = 3
opcoesNum = {
    1: "Valor 1",
    2: "Valor 2",
    3: "Valor 3",
    4: "Valor 4",
    5: "Valor 5"
}

print("______________")
print(opcoesNum[variavel])





























x = [1, 2, 3]
x.append([4, 5])
print (x)

# gives you: [1, 2, 3, [4, 5]]

# extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)

# gives you: [1, 2, 3, 4, 5]