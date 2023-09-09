# Faça uma classe que leia um número inteiro e imprima os 50 números anteriores 
#e os 50 números posteriores. 

# Função para ler um número inteiro da entrada padrão


class NumerosAnterioresEPosteriores: # Nome da classe
    def __init__(self): # Método construtor, chamado quando a classe é instanciada, ou seja, quando um objeto é criado a partir dela
        pass # Não faz nada por enquanto

    def ler_numero(self): # Método para ler um número inteiro
        try: # Tenta executar o código abaixo
            self.numero = int(input("Digite um número inteiro: ")) # Lê um número inteiro e armazena na variável self.numero
        except ValueError: # Se o usuário digitar um valor inválido, executa o código abaixo
            print("Por favor, digite um número inteiro válido.") # Imprime uma mensagem de erro

    def imprimir_numeros_anteriores_e_posteriores(self): # Método para imprimir os 50 números anteriores e posteriores
        if hasattr(self, 'numero'): # Se o objeto tiver o atributo self.numero
            numeros_anteriores = list(range(self.numero - 50, self.numero)) # Cria uma lista com os 50 números anteriores
            numeros_posteriores = list(range(self.numero + 1, self.numero + 51)) # Cria uma lista com os 50 números posteriores

            print(f"50 números anteriores a {self.numero}: {numeros_anteriores}") # Imprime os 50 números anteriores
            print(f"50 números posteriores a {self.numero}: {numeros_posteriores}") # Imprime os 50 números posteriores
        else:
            print("Você precisa digitar um número antes de imprimir os números anteriores e posteriores.") # Imprime uma mensagem de erro

# Criar uma instância da classe
calculadora = NumerosAnterioresEPosteriores() # Cria um objeto a partir da classe NumerosAnterioresEPosteriores

# Ler um número inteiro
calculadora.ler_numero() # Chama o método ler_numero do objeto calculadora

# Imprimir os 50 números anteriores e posteriores 
calculadora.imprimir_numeros_anteriores_e_posteriores()  # Chama o método imprimir_numeros_anteriores_e_posteriores do objeto calculadora
2.