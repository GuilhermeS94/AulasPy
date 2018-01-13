"""
Inicializando com Python:
    Olá mundo
    Tipos de variáveis e o que são
    e SE..., SENÃO...
    Pegando itens das listas e dicionários
"""
# 1 - ola mundo
print("Olá Python")

# 2 - imprimir Variavel
strVariavel = "Olá Python"
print(strVariavel)
# maneira 2
print("Variável: ", strVariavel, "1", "\n", [(2+3),5,8,"Oi"])
# maneira 3
print("Variável format: {}".format(strVariavel))

#strVariavel = ""
# 3 - e SE...
if not strVariavel.strip():
    print("Variável vazia")
elif strVariavel == "Olá Python":
    print("Váriável com mesmo valor de inicialização")
else:
    print("Else: {}".format(strVariavel))

# 4 - Tipos de variáveis
# e inicialização
cVariavel = 'W'
strVariavel = "Olá Python"
intVariavel = 123
decVariavel = 123.123
boolVariavel = True
listVariavel = list()
dicVariavel = dict()

print("Variáveis:\n", cVariavel, "\n", strVariavel, "\n", intVariavel,
"\n", decVariavel, "\n", boolVariavel, "\n", listVariavel, "\n", dicVariavel)

boolVariavel = (intVariavel < 0)
listVariavel = [1,2,3,4,5,6,7,8,9,10]
dicVariavel = {"key1" : "valor 1", "key2": "valor 2", 3 : 3}

print("Variáveis:\n", cVariavel, "\n", strVariavel, "\n", intVariavel,
"\n", decVariavel, "\n", boolVariavel, "\n", listVariavel, "\n", dicVariavel)

# 5 - pegando valores de listas e dicionários
print("Char da string: ", strVariavel[3])
print("Item da lista: ", listVariavel[5])
print("Item do dicionário: ", dicVariavel["key1"])
print("Item do dicionário: ", dicVariavel[3])


# Especial Chars
# ASCII to CHAR
chr(97)
# Char to ASCII
ord(cVariavel)