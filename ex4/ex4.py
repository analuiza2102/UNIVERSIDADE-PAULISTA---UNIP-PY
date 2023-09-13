class IdadeEmDias:
    def __init__(self, anos, meses, dias):
        self.anos = anos
        self.meses = meses
        self.dias = dias

    def calcular_idade_em_dias(self):
        # Converter anos e meses em dias
        total_dias = self.anos * 365 + self.meses * 30 + self.dias
        return total_dias

# Solicitar entrada do usuário para idade em anos, meses e dias
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

# Criar um objeto da classe IdadeEmDias
idade = IdadeEmDias(anos, meses, dias)

# Calcular a idade em dias
idade_em_dias = idade.calcular_idade_em_dias()

# Imprimir a idade em dias
print(f"A idade em dias é: {idade_em_dias} dias")
