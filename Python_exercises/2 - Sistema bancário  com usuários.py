import sys
from datetime import datetime

contas = []
transacao_limite = 10

def realizar_deposito():
    global conta_ativa

    if conta_ativa['Hora primeira transação'] is None:
        conta_ativa['Hora primeira transação'] = datetime.now()
    elif datetime.now() >= conta_ativa['Hora primeira transação'] + timedelta(days=1):
        conta_ativa['transacoes'] = 0
        conta_ativa['Hora primeira transação'] = datetime.now()

    if conta_ativa['transacoes'] < transacao_limite:
        valor = float(input('Deseja realizar um depósito de qual valor? R$ '))
        conta_ativa['saldo'] += valor
        conta_ativa['depósitos'].append(valor)
        conta_ativa['Horários dos depósitos'].append(datetime.now())
        conta_ativa['transacoes'] += 1

        print(f'Depósito de R${valor:.2f} registrado com sucesso!')
        print(f'Saldo total agora é R${conta_ativa["saldo"]:.2f}')
        print(f'Transações restantes: {transacao_limite - conta_ativa["transacoes"]}')
    else:
        print('Você já utilizou o limite de transações do dia. Tente novamente amanhã.')


def realizar_saque():
    global conta_ativa

    if conta_ativa['Hora primeira transação'] is None:
        conta_ativa['Hora primeira transação'] = datetime.now()
    elif datetime.now() >= conta_ativa['Hora primeira transação'] + timedelta(days=1):
        conta_ativa['transacoes'] = 0
        conta_ativa['Hora primeira transação'] = datetime.now()

    if conta_ativa['transacoes'] < transacao_limite:
        valor = float(input('Deseja realizar um saque de qual valor? R$ '))
        if valor <= conta_ativa['saldo']:
            conta_ativa['saldo'] -= valor
            conta_ativa['saques'].append(valor)
            conta_ativa['Horários dos saques'].append(datetime.now())
            conta_ativa['transacoes'] += 1

            print(f'Saque de R${valor:.2f} realizado com sucesso!')
            print(f'Saldo atual: R${conta_ativa["saldo"]:.2f}')
        else:
            print('Saldo insuficiente!')
    else:
        print('Você já utilizou o limite de transações do dia. Tente novamente amanhã.')


def mostrar_extrato():
    global conta_ativa
    print("\n--- Extrato ---")

    print("Depósitos:")
    for deposito, horario in zip(conta_ativa['depósitos'], conta_ativa['Horários dos depósitos']):
        print(f"R$ {deposito:.2f} - {horario.strftime('%Y-%m-%d %H:%M:%S')}")

    print("Saques:")
    for saque, horario in zip(conta_ativa['saques'], conta_ativa['Horários dos saques']):
        print(f"R$ {saque:.2f} - {horario.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"Saldo atual: R$ {conta_ativa['saldo']:.2f}")
    print(f"Transações restantes hoje: {transacao_limite - conta_ativa['transacoes']}")


def listar_contas_por_cpf(cpf):
    contas_existentes = encontrar_contas_por_cpf(cpf)

    if not contas_existentes:
        print("Nenhuma conta encontrada para este CPF.")
        return

    print(f"Contas associadas ao CPF {cpf}:")
    for conta in contas_existentes:
        print(f"Conta: {conta['numero_conta']}, Agência: {conta['agencia']}, Saldo: R$ {conta['saldo']:.2f}")


def encontrar_contas_por_cpf(cpf):
    return [conta for conta in contas if conta['cpf'] == cpf]


def criar_conta():
    cpf = input("Qual o número de seu CPF? ")
    contas_existentes = encontrar_contas_por_cpf(cpf)

    if contas_existentes:
        print("Este CPF já está cadastrado.")
        resposta = input("Deseja criar uma nova conta vinculada a este CPF? (s/n): ")
        if resposta.lower() == 's':
            numero_conta = f"{len(contas_existentes) + 1:04}"
            agencia = "0001"
            nova_conta = {
                "cpf": cpf,
                "nome": contas_existentes[0]["nome"],
                "data_nascimento": contas_existentes[0]["data_nascimento"],
                "endereco": contas_existentes[0]["endereco"],
                "numero_conta": numero_conta,
                "agencia": agencia,
                "saldo": 0,
                "transacoes_restantes": transacao_limite,
                "transacoes": 0,
                "extrato": [],
                "depósitos": [],
                "saques": [],
                "Horários dos depósitos": [],
                "Horários dos saques": [],
                "Hora primeira transação": None
            }
            contas.append(nova_conta)
            print(f"Conta criada com sucesso para {nova_conta['nome']}!")
            print(f"Número da conta: {nova_conta['numero_conta']}, Agência: {nova_conta['agencia']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        return

    nome = input("Qual o seu nome? ")

    dia = input("Qual o dia do seu nascimento? (dd): ")
    mes = input("Qual o mês do seu nascimento? (mm): ")
    ano = input("Qual o ano do seu nascimento? (yyyy): ")
    data_nascimento = f"{dia}/{mes}/{ano}"

    endereco = input("Por favor, digite seu endereço.\nRua: ")
    numero = input("Número: ")
    cidade = input("Cidade: ")
    estado = input("Digite as siglas de seu estado (Exemplo: SP): ")
    endereco_completo = f"{endereco}, {numero}, {cidade} - {estado}"
    numero_conta = f"{len(contas) + 1:04}"
    agencia = "0001"

    nova_conta = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco_completo,
        "numero_conta": numero_conta,
        "agencia": agencia,
        "saldo": 0,
        "transacoes_restantes": transacao_limite,
        "transacoes": 0,
        "extrato": [],
        "depósitos": [],
        "saques": [],
        "Horários dos depósitos": [],
        "Horários dos saques": [],
        "Hora primeira transação": None
    }
    contas.append(nova_conta)
    print(f"Conta criada com sucesso para {nome}!")
    print(f"Número da conta: {numero_conta}, Agência: {agencia}")
    print('Atenção!'
          '\nPara utilizar uma conta, deve selecioná-la na tela principal!'
          '\nCaso esteja dentro do menu e deseja retornar à tela principal,'
          '\nutilize a opção 4 (trocar conta) do menu principal.')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def entrar_no_sistema():
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("                        BANCO DIO                          ")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    while True:
        cpf = input("Para entrar em sua conta, digite o número de seu CPF (ou digite 'sair' para encerrar): ")

        if cpf.lower() == 'sair':
            print("Saindo do sistema...")
            break

        contas_existentes = encontrar_contas_por_cpf(cpf)

        if not contas_existentes:
            print("CPF não encontrado. Deseja tentar novamente? (s/n): ")
            resposta = input().strip().lower()
            if resposta == 's':
                continue
            else:
                print("Deseja criar uma conta nova? (s/n): ")
                resposta = input().strip().lower()
                if resposta == 's':
                    criar_conta()
                    continue
                else:
                    print("Saindo do sistema...")
                    break


        print("Contas encontradas para este CPF:")
        for i, conta in enumerate(contas_existentes, start=1):
            print(f"[{i}] Conta: {conta['numero_conta']}, Agência: {conta['agencia']}")

        opcao_conta = int(input("Escolha o número da conta que deseja usar: "))

        if 1 <= opcao_conta <= len(contas_existentes):
            conta_selecionada = contas_existentes[opcao_conta - 1]
            print(
                f"Você selecionou a conta {conta_selecionada['numero_conta']} da agência {conta_selecionada['agencia']}.")


            menu_principal(conta_selecionada)
            break
        else:
            print("Opção inválida! Tente novamente.")


def menu_principal(conta_ativa):
    print(f'Olá, {conta_ativa["nome"]}')
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        opcao = int(input('''\
Qual opção deseja?
[1] Depositar
[2] Sacar
[3] Extrato
[4] Trocar conta
[5] Criar nova conta
[6] Listar contas por CPF
[7] Sair
=> '''))

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            conta_ativa['saldo'] += valor
            conta_ativa['transacoes_restantes'] -= 1
            data_hora = datetime.now()
            conta_ativa['extrato'].append((f"Depósito de R$ {valor:.2f}", data_hora))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso em {data_hora.strftime('%d-%m-%Y %H:%M:%S')}.")
            print(f"Transações restantes: {conta_ativa['transacoes_restantes']}")

        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            if conta_ativa['saldo'] >= valor:
                conta_ativa['saldo'] -= valor
                conta_ativa['transacoes_restantes'] -= 1
                data_hora = datetime.now()
                conta_ativa['extrato'].append((f"Saque de R$ {valor:.2f}", data_hora))
                print(f"Saque de R$ {valor:.2f} realizado com sucesso em {data_hora.strftime('%d-%m-%Y %H:%M:%S')}.")
            else:
                print("Saldo insuficiente!")
            print(f"Transações restantes: {conta_ativa['transacoes_restantes']}")

        elif opcao == 3:
            if not conta_ativa['extrato']:
                print("Nenhuma transação realizada.")
            else:
                print("Extrato da conta:")
                for item, data_hora in conta_ativa['extrato']:
                    print(f"{item} - {data_hora.strftime('%d-%m-%Y %H:%M:%S')}")

        elif opcao == 4:
            print("Trocando de conta...")
            entrar_no_sistema()

        elif opcao == 5:
            criar_conta()

        elif opcao == 6:
            cpf = input("Digite o CPF para listar as contas: ")
            listar_contas_por_cpf(cpf)

        elif opcao == 7:
            print("Encerrando o sistema...")
            sys.exit()

        else:
            print("Opção inválida!")


# Inicia o sistema
entrar_no_sistema()