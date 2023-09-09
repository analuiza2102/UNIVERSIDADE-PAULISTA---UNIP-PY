#Faça uma classe que leia a idade de uma pessoa em ano, meses e dias e imprima a idade em dias. Considerar ano com 365 dias e mês com 30 dias. 

class IdadeEmDias:
    def __init__(self):
        pass

    def ler_idade(self):
        while True:
            try:
                self.anos = int(input("Digite a idade em anos: "))
                self.meses = int(input("Digite a idade em meses: "))
                break  # Sai do loop se todas as conversões forem bem-sucedidas
            except ValueError:
                print("Erro: Por favor, digite valores inteiros válidos.")

    def calcular_idade_em_dias(self):
        if hasattr(self, 'anos') and hasattr(self, 'meses'):
            idade_em_dias = (self.anos * 365) + (self.meses * 30)
            print(f"A idade em dias é: {idade_em_dias} dias")
        else:
            print("Você precisa digitar a idade em anos e meses antes de calcular a idade em dias.")

# Criar uma instância da classe
calculadora = IdadeEmDias()

# Ler a idade em anos e meses com verificação de entrada
calculadora.ler_idade()

# Calcular e imprimir a idade em dias
calculadora.calcular_idade_em_dias()


