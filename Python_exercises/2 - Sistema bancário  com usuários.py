import time
from time import sleep

saldo_total = 0
limite = 500
extrato_saques = []
extrato_depositos = []
numero_saques = 0
limite_saques = 3


print('-=' * 30)
print('BANCO DIO'.center(58))
print('-=' * 30)
menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

time.sleep(0.5)
while True:

    print('-=' * 30)
    print('Qual opção deseja?')

    opcao = int(input(menu))
    print(f'A opção escolhida foi: [{opcao}]', end=' ')

    if opcao == 1:
        time.sleep(0.5)
        print('-=' * 30)
        print('Depósito'.center(58))
        print('-=' * 30)
        valor = float(input('Deseja realizar um depósito de qual valor? R$ '))
        extrato_depositos.append(valor)
        saldo_total += valor
        print(f'Depósito de  R${valor:.2f} registrado. \nAgora, seu saldo total é R${saldo_total:.2f}')
        time.sleep(0.5)

    if opcao == 2:
        time.sleep(0.5)
        print('-=' * 30)
        print('Saque'.center(58))
        print('-=' * 30)
        if saldo_total > 0:
            if limite_saques > numero_saques:
                valor = float(input('Deseja realizar um saque de qual valor? R$ '))
                if valor > 500:
                    while valor > 500:
                        print('Não é possível fazer um saque acima de R$500. '
                              'Digite um outro valor.')
                        valor = float(input('Deseja realizar um saque de qual valor? R$ '))
                        if valor < 500:
                            break

                extrato_saques.append(valor)
                saldo_total -= valor
                numero_saques += 1
                print(f'Saque no valor de  R${valor:.2f} registrado.'
                 f'\nAgora, seu saldo total é R${saldo_total:.2f}'
                 f'\nJá foram realizados {numero_saques} saques hoje.'
                 f'\nVocê possui mais {limite_saques - numero_saques} saques restantes.')
            else:
                print('Você já utilizou seu limites de saques do dia. '
                      '\nTente novamente amanhã!')
        else:
            print('Opção inválida! Você não possui saldo!')
        time.sleep(0.5)

    if opcao == 3:
        time.sleep(0.5)

        print('-=' * 30)
        print('Extrato'.center(58))
        print('-=' * 30)

        if len(extrato_saques) > 0:
            print(f'Até o momento, você realizou os seguintes saques: ')
            for n in extrato_saques:
                print(f'R${n:.2f}')

        else:
            print('Ainda não foram realizados saques.')

        if len(extrato_depositos) > 0:
            print(f'Até o momento, você realizou os seguintes depósitos: ')
            for n in extrato_depositos:
                print(f'R${n:.2f}')

        else:
            print('Ainda não foram realizados depósitos.')

        print(f'Neste momento, seu saldo total é R${saldo_total:.2f}')

        time.sleep(0.5)

    if opcao == 4:
        print('-=' * 30)
        print('\nEncerrando',end='')
        for n in range(0, 3):
            print('.', end='')
            time.sleep(0.3)
        print()
        break

    if opcao <= 0 or opcao > 4:
        print('Opção inválida! Tente novamente! ')
        time.sleep(0.5)

print('Agradecemos pela preferência!')
