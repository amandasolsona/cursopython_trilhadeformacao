# Calculo de IMC - Índice de Massa Corporal
# Menor que 18.5: Magreza
# Entre 18.5 e 24.9: Normal
# Entre 25.0 e 29.9: Sobrepeso
# Entre 30.0 e 39.9: Obesidade
# Maior que 40.0: Obesidade Grave

print('######## CALCULADORA IMC - ÍNDICE DE MASSA CORPORAL ########')
peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura em cm: '))
altura_cm_para_metro = float(altura / 100)
calculo_imc = peso / (altura_cm_para_metro* altura_cm_para_metro)

if calculo_imc < 18.5:
    print(f'Você encontra-se em situação de magreza, conforme seu imc {calculo_imc:0.2f}')
elif 18.5 <= calculo_imc <= 24.9:
    print(f'Você encontra-se em situação normal, conforme seu imc {calculo_imc:0.2f}')
elif 25.0 <= calculo_imc <= 29.9:
    print(f'Você encontra-se em situação de sobrepeso, conforme seu imc {calculo_imc:0.2f}')
elif 30.0 <= calculo_imc <= 39.9:
    print(f'Você encontra-se em situação de obesidade, conforme seu imc {calculo_imc:0.2f}')
else:
    print(f'Você encontra-se em situação de obesidade grave, conforme seu imc {calculo_imc:0.2f}')


