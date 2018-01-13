"""
Digitando.
Repetindo as coisas:
calma, analise, e PENSE!
Algo está ERRADO!
"""

variavel = 5
variavel2 = 10

print("Soma 1 = ", variavel + variavel2)

variavel = 7
variavel2 = 3

print("Soma 2 = ", variavel + variavel2)

variavel = 0
variavel2 = 0

try:
    variavel = int(input("Digite um número: "))
    variavel2 = 12589
except Exception as ex:
    print(ex)

print("Soma 3 = ", variavel + variavel2)

def SomaDoisNumeros(valor1, valor2):
    return (valor1 + valor2)


variavel = 1
variavel2 = 2

print("Soma Def = ", SomaDoisNumeros(variavel, variavel2))

variavel = 3
variavel2 = 3

print("Soma Def 2 = ", SomaDoisNumeros(variavel, variavel2))

def NomeCompleto(nome, sobrenome):
    return "{} {}".format(nome, sobrenome)

meuNome = input("Digite seu nome: ")
meuSobreNome = input("Digite seu sobrenome: ")

print("Nome completo: {}".format(NomeCompleto(meuNome, meuSobreNome)))