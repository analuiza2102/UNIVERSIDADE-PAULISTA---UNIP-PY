# Faça uma classe que receba três números com decimais e imprima o maior deles.

class MaiorNumero:
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

    def encontrar_maior(self):
        if hasattr(self, 'numero1') and hasattr(self, 'numero2') and hasattr(self, 'numero3'): #hasattr() é uma função interna do Python que verifica se um objeto tem um atributo específico.
            maior = self.numero1
            if self.numero2 > maior:
                maior = self.numero2
            if self.numero3 > maior:
                maior = self.numero3

            print(f"O maior número é: {maior}")
        else:
            print("Você precisa digitar os três números decimais antes de encontrar o maior.")

# Criar uma instância da classe
calculadora = MaiorNumero()

# Ler os números decimais com verificação de entrada
calculadora.ler_numeros()

# Encontrar e imprimir o maior número
calculadora.encontrar_maior()




#instrucao para digitar o comando no terminal
#1 - Digite o primeiro número decimal: exemplo 3.15
#2 - Digite o segundo número decimal: exemplo 2.15
#3 - Digite o terceiro número decimal: exemplo 1.15

#So usamos "." para numeros decimais, para numeros inteiros usamos ",", pois o python entende que "." é um separador de casas decimais


"""A função float(input()) tentará converter essa string em um número de ponto flutuante, e ela pode fazer isso com sucesso para entradas como "10" ou "3.14", pois
 o Python permite a conversão de strings contendo números inteiros em números de ponto flutuante sem problemas.
Portanto, mesmo que você insira "10" no terminal, ele será lido como uma string e convertido para um número de ponto flutuante pelo código que forneci anteriormente. 
No entanto, em termos conceituais, "10" é considerado um número inteiro, mas o Python permite que ele seja tratado como um número de ponto flutuante quando apropriado."""