#Faça uma classe que receba três números com decimais e imprima o menor deles. 

class MenorNumero:
    def __init__(self):
        pass

    def ler_numeros(self):
        while True:
            try:
                self.numero1 = float(input("Digite o primeiro número decimal: "))
                self.numero2 = float(input("Digite o segundo número decimal: "))
                self.numero3 = float(input("Digite o terceiro número decimal: "))
                break  # Sai do loop se todas as conversões forem bem-sucedidas
            except ValueError:
                print("Erro: Por favor, digite números decimais válidos.")

    def encontrar_menor(self):
        if hasattr(self, 'numero1') and hasattr(self, 'numero2') and hasattr(self, 'numero3'):
            menor = self.numero1
            if self.numero2 < menor:
                menor = self.numero2
            if self.numero3 < menor:
                menor = self.numero3

            print(f"O menor número é: {menor}")
        else:
            print("Você precisa digitar os três números decimais antes de encontrar o menor.")

# Criar uma instância da classe
calculadora = MenorNumero()

# Ler os números decimais com verificação de entrada
calculadora.ler_numeros()

# Encontrar e imprimir o menor número
calculadora.encontrar_menor()
