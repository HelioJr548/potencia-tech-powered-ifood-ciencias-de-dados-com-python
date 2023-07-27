# Definindo a variável 'nome' com uma string contendo o nome completo
nome = "Helio de Jesus dos Santos Junior"

# Imprime o primeiro caractere da string 'nome'
print(nome[0])
# Saída: 'H'

# Imprime o penúltimo caractere da string 'nome'
print(nome[-2])
# Saída: 'o'

# Imprime os primeiros 9 caracteres da string 'nome' (do índice 0 ao índice 8)
print(nome[:9])
# Saída: 'Helio de '

# Imprime a string 'nome' a partir do 10º caractere até o final
print(nome[10:])
# Saída: 'Jesus dos Santos Junior'

# Imprime os caracteres da string 'nome' do índice 10 ao índice 15 (não inclui o índice 16)
print(nome[10:16])
# Saída: 'Jesus '

# Imprime os caracteres da string 'nome' do índice 10 ao índice 15, pulando de 2 em 2 caracteres
print(nome[10:16:2])
# Saída: 'Jss'

# Imprime toda a string 'nome' (do início ao fim)
print(nome[:])
# Saída: 'Helio de Jesus dos Santos Junior'

# Imprime a string 'nome' em ordem reversa, ou seja, de trás para frente
print(nome[::-1])
# Saída: 'roinuJ stnaS sod suseJ ed oileH'
