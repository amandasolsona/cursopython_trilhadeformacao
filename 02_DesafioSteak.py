# Crie um programa que dependendo da temperatura (em celsius) do steak
# ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.
# Temperaturas - cozimento
# 120°F ou 48°C - Rare (selada)
# 130°F ou 54°C - Medium rare (Ao ponto para o mal)
# 140°F ou 60ºC - Medium (Ao ponto)
# 150°F ou 65°C - Medium well (Ao ponto para o bem)
# 160°F ou 71°C - Well done (Bem passada)

print('######## Bem Vindo ao Restaurante X ########')
cliente_celsius = int(input('Digite a temperatura (em celsius) da carne que deseje: '))
rare = 48
medium_rare = 54
medium = 60
medium_well = 65
well_done = 71

if cliente_celsius < rare:
    print('A carne encontra-se crua. ')

elif cliente_celsius < medium_rare:
    print('A carne encontra-se selada. ')

elif cliente_celsius < medium:
    print('A carne encontra-se ao ponto para mal. ')

elif cliente_celsius < medium_well:
    print('A carne encontra-se ao ponto. ')

elif cliente_celsius < well_done:
    print('A carne encontra-se ao ponto para bem. ')

else:
    print('A carne encontra-se bem passada. ')



