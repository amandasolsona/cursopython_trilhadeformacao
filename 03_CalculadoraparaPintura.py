# Desafios com funções
# Criar um programa que calcula a quantidade de tinta necessária para
# pintar uma parede. O usuário deverá fornecer as seguintes informações:
# rendimento, altura e largura. O programa deve mostrar na tela a mensagem
# 'Você necessita de x latas de tinta'.

def calcular_area(altura, largura):
    area_calculada = float(altura * largura)
    return area_calculada


def quantidade_tinta(area, rendimento):
    quantidade_tinta_calculada = area / rendimento
    quantidade_tinta_calculada = int(quantidade_tinta_calculada) + 1
    return quantidade_tinta_calculada


entrada_rendimento = float(input('Digite o rendimento da tinta em m² por lata: '))
entrada_altura = float(input("Digite a altura da parede em metros: "))
entrada_largura = float(input("Digite a largura da parede em metros: "))

valor_area = calcular_area(entrada_altura, entrada_largura)  # chamando a função
print(f'O valor da sua área é {valor_area} m² ! ')
valor_tinta = quantidade_tinta(valor_area, entrada_rendimento)  # chamando a função
print(f"Você necessita de {valor_tinta} latas de tinta.")
