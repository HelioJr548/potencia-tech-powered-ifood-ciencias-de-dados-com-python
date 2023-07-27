nome = "HeLIo"

# (converte a string para letras maiúsculas)
print(nome.upper())  # Saída: "HELIO"

# (converte a string para letras minúsculas)
print(nome.lower())  # Saída: "helio"

# (capitaliza a primeira letra de cada palavra)
print(nome.title())  # Saída: "Helio"


texto = "  Olá mundo!    "

# (concatena um ponto ao final da string)
print(texto + ".")  # Saída: "  Olá mundo!    ."

# (remove espaços em branco no início e no final da string e concatena um ponto)
print(texto.strip() + ".")  # Saída: "Olá mundo!."

# (remove espaços em branco no final da string e concatena um ponto)
print(texto.rstrip() + ".")  # Saída: "  Olá mundo!."

# (remove espaços em branco no início da string e concatena um ponto)
print(texto.lstrip() + ".")  # Saída: "Olá mundo!    ."

menu = "Python"

# (concatena "####" no início e no final da string)
print("####" + menu + "####")  # Saída: "####Python####"

# (centraliza a string em um espaço total de 14 caracteres)
print(menu.center(14))  # Saída: "   Python   "

# (centraliza a string em um espaço total de 14 caracteres, preenchendo com "#" nos espaços)
print(menu.center(14, "#"))  # Saída: "###Python###"

# (insere um "-" entre cada caractere da string)
print("-".join(menu))  # Saída: "P-y-t-h-o-n"
