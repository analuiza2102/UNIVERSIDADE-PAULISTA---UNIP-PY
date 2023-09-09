""""Faça uma classe que entre com 10 municípios, contendo os seguintes dados para 
cada: nome, o total de eleitores, o número de votos em branco, o número de votos nulos 
e o número de votos válidos. Calcular e imprimir de acordo com a tabela abaixo: 
Município: Bauru 
Totais 
Quantidade 
Porcentagem 
Eleitores 
1.000 
100% 
Votos em branco 
250 
25% 
Votos nulos 
250 
25% 
Votos válidos 
500 
50% 
Após imprimir os dados de todos os municípios, imprimir o seguinte resumo: 
Totais 
Nome 
Quantidade 
Porcentagem 
Município com mais eleitores 
Município A 
999 
99,99% 
Município com mais votos em branco 
Município B 
250 
25% 
Município com mais votos nulos 
Município C 
250 
25% 
Município com mais votos válidos 
Município D 
500 
50%"""




from tabulate import tabulate
from colorama import Fore 

class Municipios:
    def __init__(self):
        self.municipios = []

    def registrar_municipio(self):
        nome = input("Nome do município: ")
        eleitores = int(input("Quantidade de eleitores: "))
        votos_validos = int(input("Quantidade de votos válidos: "))
        votos_brancos = int(input("Quantidade de votos em branco: "))
        votos_nulos = int(input("Quantidade de votos nulos: "))

        municipio = {
            'nome': nome,
            'eleitores': eleitores,
            'votos_validos': votos_validos,
            'votos_brancos': votos_brancos,
            'votos_nulos': votos_nulos
        }

        self.municipios.append(municipio)

    def calcular_estatisticas(self):
        for municipio in self.municipios:
            total_eleitores = municipio['eleitores']
            total_votos_validos = municipio['votos_validos']
            total_votos_brancos = municipio['votos_brancos']
            total_votos_nulos = municipio['votos_nulos']

            print("\nEstatísticas do Município:", municipio['nome'])
            data = [
                ["Quantidade Eleitores", total_eleitores, 100.0],
                ["Votos em Branco", total_votos_brancos, (total_votos_brancos / total_eleitores) * 100],
                ["Votos Nulos", total_votos_nulos, (total_votos_nulos / total_eleitores) * 100],
                ["Votos Válidos", total_votos_validos, (total_votos_validos / total_eleitores) * 100]
            ]
            headers = ["Descrição", "Quantidade", "Porcentagem"]
            print(tabulate(data, headers, tablefmt="pretty"))

    def encontrar_maximos(self):
        max_eleitores = max(self.municipios, key=lambda x: x['eleitores'])
        max_votos_validos = max(self.municipios, key=lambda x: x['votos_validos'])
        max_votos_brancos = max(self.municipios, key=lambda x: x['votos_brancos'])
        max_votos_nulos = max(self.municipios, key=lambda x: x['votos_nulos'])

        print("\nResumo:")
        data = [
            ["Município com mais eleitores", max_eleitores['nome'], max_eleitores['eleitores'], 100.0],
            ["Município com mais votos válidos", max_votos_validos['nome'], max_votos_validos['votos_validos'], (max_votos_validos['votos_validos'] / max_eleitores['eleitores']) * 100],
            ["Município com mais votos em branco", max_votos_brancos['nome'], max_votos_brancos['votos_brancos'], (max_votos_brancos['votos_brancos'] / max_eleitores['eleitores']) * 100],
            ["Município com mais votos nulos", max_votos_nulos['nome'], max_votos_nulos['votos_nulos'], (max_votos_nulos['votos_nulos'] / max_eleitores['eleitores']) * 100]
        ]
        headers = ["Totais", "Nome", "Quantidade", "Porcentagem"]
        print(tabulate(data, headers, tablefmt="pretty"))


def main():
    calculadora = Municipios()
    
    while True:
        calculadora.registrar_municipio()
        continuar = input("Deseja registrar mais um município? (S/N): ")
        if continuar.upper() != "S":
            break

    calculadora.calcular_estatisticas()
    calculadora.encontrar_maximos()


if __name__ == "__main__":
    main()

            