# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    entrada = input().strip()
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = entrada.rfind(" ")
    nome = entrada[:posicao_espaco]
    preco = float(entrada[posicao_espaco + 1:])

    # Adiciona ao carrinho
    carrinho.append((nome, preco))
    total += preco

# Exibe os itens e o total em formato esperado
for nome, preco in carrinho:
    # Formatando com "R$" e duas casas decimais
    print(f"{nome}: R${preco:.2f}")
print(f"Total: R${total:.2f}")
