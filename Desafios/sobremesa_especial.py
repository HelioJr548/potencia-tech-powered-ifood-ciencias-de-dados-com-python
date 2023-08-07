VALOR_MEDIO_PARA_BRINDE = 50


def obter_valor_valido():
    while True:
        try:
            valor = int(input("Digite o valor total do seu pedido: "))
            if valor >= 0:
                return valor
            else:
                print("Valor inválido. Digite um valor não negativo.\n")
        except ValueError:
            print("Valor inválido. Digite um número válido.\n")


def condicao_para_brinde(valor_pedido):
    if valor_pedido >= VALOR_MEDIO_PARA_BRINDE:
        print("Parabens, você ganhou uma sobremesa gratis!")
    else:
        print("Que pena, você nao ganhou nenhum brinde especial.")


condicao_para_brinde(obter_valor_valido())
