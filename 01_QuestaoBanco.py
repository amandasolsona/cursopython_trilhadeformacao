print(f'---- Bem vindo ao Banco X ----')

while True:
    print('Selecione uma opção:')
    print('1 - Abrir uma conta conosco: ')
    print('2 - Encerrar o atendimento:')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        print('Abrir a conta:')

        renda = int(input('Digite o valor da sua renda:'))

        if renda >= 5000:
            print('Renda aprovada. ')
            opcao2 = int(input('Digite a opção abaixo para situação de inadiplência: 1 - Negativado e '
                               '2 - não negativado'))
            if opcao2 == 1:
                print('Você não poderá abrir a conta conosco, pois encontra-se negativado. ')
            else:
                print('Você poderá abrir a conta conosco.')

        else:
            print('Renda reprovada. Você não poderá abrir uma conta conosco')

    else:
        print('Atendimento encerrado')
