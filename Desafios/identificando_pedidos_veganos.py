def main():
    n = int(input())
    
    pedidos = []
    
    for i in range(n):
        nome_prato = input()
        calorias = int(input())
        eh_vegano = input()
        
        if eh_vegano == "s":
            tipo_vegano = "Vegano"
        else:
            tipo_vegano = "Não-vegano"
        
        pedidos.append((nome_prato, calorias, tipo_vegano))
    
    for i, pedido in enumerate(pedidos, start=1):
        nome_prato, calorias, tipo_vegano = pedido
        print(f"Pedido {i}: {nome_prato} ({tipo_vegano}) - {calorias} calorias")

if __name__ == "__main__":
    main()
