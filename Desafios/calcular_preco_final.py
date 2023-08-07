def calcular_total_pedido(
    valor_hamburguer, quantidade_hamburguer, valor_bebida, quantidade_bebida
):
    return valor_hamburguer * quantidade_hamburguer +valor_bebida * quantidade_bebida

def calcular_troco(valor_pago, total_pedido):
    return valor_pago - total_pedido



def obter_valor_valido(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("Valor inválido. Digite um valor não negativo.\n")
        except ValueError:
            print("Valor inválido. Digite um número válido.\n")
        


valor_hamburguer = obter_valor_valido("Digite o valor do hambúrguer: ")
quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres: "))
valor_bebida = obter_valor_valido("Digite o valor da bebida: ")
quantidade_bebida = int(input("Digite a quantidade de bebidas: "))
valor_pago = obter_valor_valido("Digite o valor pago: ")

total_pedido = calcular_total_pedido(
    valor_hamburguer, quantidade_hamburguer, valor_bebida, quantidade_bebida
)

troco_pedido = calcular_troco(valor_pago, total_pedido)

print(
    f"O preço final do pedido é R$ {total_pedido:.2f}. Seu troco é R$ {troco_pedido:.2f}."
)
