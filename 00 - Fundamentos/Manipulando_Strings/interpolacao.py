nome = "Helio"
idade = 20
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Helio", "idade": 28}

# Usando formatação com símbolos de porcentagem (%)
print("Nome: %s Idade: %d" % (nome, idade))
# Saída: Nome: Helio Idade: 20

# Usando o método format() sem especificar os índices
print("Nome: {} Idade: {}".format(nome, idade))
# Saída: Nome: Helio Idade: 20

# Especificando os índices na ordem desejada dentro das chaves do método format()
print("Nome: {1} Idade: {0}".format(idade, nome))
# Saída: Nome: Helio Idade: 20

# Repetindo os índices em diferentes posições
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
# Saída: Nome: Helio Idade: 20 Nome: Helio Helio Helio

# Usando o método format() com argumentos nomeados
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# Saída: Nome: Helio Idade: 20

# Usando o método format() com argumentos nomeados e repetindo os valores
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
# Saída: Nome: Helio Idade: 20 Helio Helio 20

# Usando o método format() com argumentos nomeados e passando um dicionário
print("Nome: {nome} Idade: {idade}".format(**dados))
# Saída: Nome: Helio Idade: 28

# Utilizando f-strings (formatted string literals) - disponível a partir do Python 3.6
print(f"Nome: {nome} Idade: {idade}")
# Saída: Nome: Helio Idade: 20

# Utilizando f-strings e formatando o valor do saldo com duas casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# Saída: Nome: Helio Idade: 20 Saldo: 45.44

# Utilizando f-strings e formatando o valor do saldo com um espaço total de 10 caracteres (alinhamento à direita)
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
# Saída: Nome: Helio Idade: 20 Saldo:       45.4
