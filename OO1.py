"""Listando as Pessoas"""

from Modelos.Pessoas import Pessoas


print("-----------------------------Ini processo-----------------------------")
listaPessoas = Pessoas().ListarTodos(pAtivo=True)

for pessoa in listaPessoas:
    print(pessoa.__dict__)

print("-----------------------------Fim processo-----------------------------")