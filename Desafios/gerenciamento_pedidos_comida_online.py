def calcular_valor_pedido(pedidos):
    valor_total_pedido = 0
    for pedido in pedidos:
        valor_total_pedido += float(pedido[1])
    return valor_total_pedido

def aplicar_desconto(cupom_desconto, valor_total_pedido):
    if cupom_desconto == "10%":
        desconto = 0.9
    elif cupom_desconto == "20%":
        desconto = 0.8
    else:
        desconto = 1.0
    return  valor_total_pedido * desconto

def main():
    quantidade_item_pedido = int(input())
    
    pedidos = [input().split() for _ in range(quantidade_item_pedido)]
    
    valor_total_pedido = calcular_valor_pedido(pedidos)
    
    cupom_desconto = input()
    
    valor_desconto_aplicado = aplicar_desconto(cupom_desconto, valor_total_pedido)
    
    print(f"Valor total: {valor_desconto_aplicado:.2f}")

if __name__ == "__main__":
    main()
