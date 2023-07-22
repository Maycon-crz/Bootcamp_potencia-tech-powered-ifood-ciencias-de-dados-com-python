nome = "Maycon"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Maycon", "idade": 24}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))