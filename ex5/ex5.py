from tabulate import tabulate
from colorama import Fore

class Municipios:
    def __init__(self):
        self.municipios = []

    def registrar_municipio(self):
        nome = input("Nome do município: ")
        votos_validos = int(input("Quantidade de votos válidos: "))
        votos_brancos = int(input("Quantidade de votos em branco: "))
        votos_nulos = int(input("Quantidade de votos nulos: "))

        municipio = {
            'nome': nome,
            'votos_validos': votos_validos,
            'votos_brancos': votos_brancos,
            'votos_nulos': votos_nulos
        }

        self.municipios.append(municipio)

    def calcular_estatisticas(self):
        for municipio in self.municipios:
            total_votos_validos = municipio['votos_validos']
            total_votos_brancos = municipio['votos_brancos']
            total_votos_nulos = municipio['votos_nulos']

            print(Fore.GREEN + "\nEstatísticas do Município:", municipio['nome'] + Fore.RESET)
            data = [
                ["Votos em Branco", total_votos_brancos, f"{(total_votos_brancos / total_votos_validos) * 100:.2f}%"],
                ["Votos Nulos", total_votos_nulos, f"{(total_votos_nulos / total_votos_validos) * 100:.2f}%"],
                ["Votos Válidos", total_votos_validos, "100%"]
            ]
            headers = ["Descrição", "Quantidade", "Porcentagem"]
            print(tabulate(data, headers, tablefmt="pretty"))

    def encontrar_maximos(self):
        max_votos_validos = max(self.municipios, key=lambda x: x['votos_validos'])
        max_votos_brancos = max(self.municipios, key=lambda x: x['votos_brancos'])
        max_votos_nulos = max(self.municipios, key=lambda x: x['votos_nulos'])

        print(Fore.BLUE + "\nResumo:" + Fore.RESET)
        data = [
            ["Município com mais votos válidos", max_votos_validos['nome'], max_votos_validos['votos_validos'], f"{(max_votos_validos['votos_validos'] / max_votos_validos['votos_validos']) * 100:.2f}%"],
            ["Município com mais votos em branco", max_votos_brancos['nome'], max_votos_brancos['votos_brancos'], f"{(max_votos_brancos['votos_brancos'] / max_votos_validos['votos_validos']) * 100:.2f}%"],
            ["Município com mais votos nulos", max_votos_nulos['nome'], max_votos_nulos['votos_nulos'], f"{(max_votos_nulos['votos_nulos'] / max_votos_validos['votos_validos']) * 100:.2f}%"]
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
