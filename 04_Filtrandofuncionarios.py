# Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:
# Lista1 = Funcionários que tem carro e trabalham a noite
# Lista2 = Funcionários que tem carro e trabalham durante o dia
# Lista3 = Funcionários que não tem carro

funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista1 = tem_carro.intersection(turno_noite)
print(f'Esses são os funcionários que possuem carro e são do turno da noite: {lista1}. ')

lista2 = tem_carro.intersection(turno_dia)
print(f'Esses são os funcionários que possuem carro e são do turno da manhã: {lista2}. ')

lista3 = funcionarios.difference(tem_carro)
print(f'Esses são os funcionários que não possuem carro: {lista3}. ')