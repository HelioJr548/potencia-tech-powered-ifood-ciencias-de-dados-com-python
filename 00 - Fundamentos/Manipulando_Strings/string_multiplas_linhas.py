# Definindo a variável 'nome' com uma string contendo o nome "Helio"
nome = "Helio"

# Utilizando uma f-string para criar uma mensagem formatada com variável 'nome' e recuos
mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

# Imprime a mensagem formatada com a variável 'nome' e recuos
print(mensagem)
# Saída:
#   Olá meu nome é Helio,
# Eu estou aprendendo Python.
#      Essa mensagem tem diferentes recuos.

# Imprime um menu com várias opções formatadas com recuos
print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)
# Saída:
#     ============= MENU =============
#
#     1 - Depositar
#     2 - Sacar
#     0 - Sair
#
#     ================================
#
#             Obrigado por usar nosso sistema!!!!
