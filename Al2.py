"""
Laços de repetição
"""

# Imprime 0,1,2,3,4
# 1 em 1, < 5
for x in range(5):
    print(x)
print("\n")
# Imprime 3,4,5
# 1 em 1, de 3 até < 5
for x in range(3, 6):
    print(x)
print("\n")
# Imprime 3,5,7
# 2 em 2, de 3 até < 8
for x in range(3, 8, 2):
    print(x)
print("\n")
# com string também funfa
for c in "Palavras":
    print(c)
print("\n")

# Imprime -5 até -8
# -1 em -1 > -9
for x in range(-5, -9, -1):
    print(x)

print("\n")   
# enquanto VERDADEIRO, FAÇA...
# caso seja variável numérica, incremento
# deve ser feito de maneira MANUAL
variavel = 0
while variavel < 8:
    print(variavel)
    variavel += 1
    # variavel = variavel + 1
    # comum mas não "existe no PYTHON"
    # variavel++ X