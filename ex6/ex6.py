class CalculadoraCompra:
    def __init__(self):
        self.produtos = []

    def ler_dados_produto(self):
        for i in range(10):
            descricao = input(f"Digite a descrição do produto {i+1}: ")
            quantidade = int(input(f"Digite a quantidade adquirida do produto {i+1}: "))
            preco_unitario = float(input(f"Digite o preço unitário do produto {i+1}: "))
            
            produto = {
                'descricao': descricao,
                'quantidade': quantidade,
                'preco_unitario': preco_unitario
            }
            self.produtos.append(produto)

    def calcular_total(self):
        for produto in self.produtos:
            quantidade = produto['quantidade']
            preco_unitario = produto['preco_unitario']
            
            total = quantidade * preco_unitario
            desconto = 0.0

            if quantidade <= 5:
                desconto = total * 0.02
            elif quantidade > 5 and quantidade <= 10:
                desconto = total * 0.03
            else:
                desconto = total * 0.05
            
            total_a_pagar = total - desconto

            produto['total'] = total
            produto['desconto'] = desconto
            produto['total_a_pagar'] = total_a_pagar

    def imprimir_resultados(self):
        print("\nDetalhes da Compra:")
        for produto in self.produtos:
            print(f"Descrição do Produto: {produto['descricao']}")
            print(f"Quantidade Adquirida: {produto['quantidade']}")
            print(f"Preço Unitário: R$ {produto['preco_unitario']:.2f}")
            print(f"Total: R$ {produto['total']:.2f}")
            print(f"Desconto: R$ {produto['desconto']:.2f}")
            print(f"Total a Pagar: R$ {produto['total_a_pagar']:.2f}")
            print()

# Criar uma instância da classe
calculadora = CalculadoraCompra()

# Ler os dados dos produtos
calculadora.ler_dados_produto()

# Calcular total, desconto e total a pagar
calculadora.calcular_total()

# Imprimir resultados
calculadora.imprimir_resultados()



"""Descrição do Produto: Camiseta
Quantidade Adquirida: 7
Preço Unitário: R$ 20.00
Produto 2:

Descrição do produto (nome): Sapato
Quantidade adquirida do produto: 4
Preço unitário do produto: R$ 50.00
Produto 3:

Descrição do produto (nome): Calça Jeans
Quantidade adquirida do produto: 12
Preço unitário do produto: R$ 60.00
Produto 4:

Descrição do produto (nome): Blusa de Inverno
Quantidade adquirida do produto: 3
Preço unitário do produto: R$ 45.00
Produto 5:

Descrição do produto (nome): Tênis Esportivo
Quantidade adquirida do produto: 9
Preço unitário do produto: R$ 80.00
Produto 6:

Descrição do produto (nome): Celular
Quantidade adquirida do produto: 6
Preço unitário do produto: R$ 800.00
Produto 7:

Descrição do produto (nome): Mochila
Quantidade adquirida do produto: 2
Preço unitário do produto: R$ 40.00
Produto 8:

Descrição do produto (nome): Óculos de Sol
Quantidade adquirida do produto: 15
Preço unitário do produto: R$ 25.00
Produto 9:

Descrição do produto (nome): Livro
Quantidade adquirida do produto: 8
Preço unitário do produto: R$ 15.00
Produto 10:

Descrição do produto (nome): Fone de Ouvido
Quantidade adquirida do produto: 1
Preço unitário do produto: R$ 30.00
"""