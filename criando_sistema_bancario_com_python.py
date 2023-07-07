from operator import itemgetter

menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
transacoes = []

while True:

    opcao = input (menu)

    if opcao == '1':
        deposito = float (input ('Por favor insira o valor do Depósito: R$ '))
        if deposito < 0:
            print ('Por favor informe um valor válido!')
        else:
            transacoes.append (['Depósito', deposito])
            saldo += deposito
            print ('Depósito Efetuado')
    
    elif opcao == '2':
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float (input ('Por favor insira o valor do Saque: R$ '))
            if valor_saque < 0:
                print ('Por favor informe um valor válido!')
            elif valor_saque > limite:
                print (f'Por favor insira um valor válido dentro do seu limite diário de R$ {limite:,.2f}')
            else:
                if saldo >= valor_saque:
                    transacoes.append (['Saque', valor_saque])
                    saldo -= valor_saque
                    numero_saques += 1
                    print (f'Realizado saque de R$ {valor_saque:,.2f}')
                else:
                    print ('Você não tem saldo suficiente para realizar essa operação.')
        else:
            print (f'Você já atingiu o limite máximo de {LIMITE_SAQUES} saques permitidos por dia')
    
    elif opcao == '3':
            def formatar (transacoes, cols_sizes):
                col1_size, col2_size, col3_size, col4_size = itemgetter ('col1_size', 'col2_size', 'col3_size', 'col4_size')(cols_sizes)
                print (f'{"EXTRATO":^60}')
                print ('-' * 60)
                print (f'{"Nr.":{col1_size}} {"TRANSAÇÃO":<{col2_size}} {"VALOR":>{col4_size}}')
                print ('-' * 60)
                for i, transacao in enumerate (transacoes, start=1):             
                    print (f'{i:>{col1_size}} {transacao [0]:<{col2_size}} {"R$":>{col3_size}} {transacao [1]:>{col4_size - 3},.2f}')

            if len (transacoes) == 0:
                formatar (transacoes, { 'col1_size': 3, 'col2_size': 26, 'col3_size': 5, 'col4_size': 16})
                print (f'{"NÃO HOUVE MOVIMENTAÇÃO NA CONTA":^60}')
                print ('-' * 60)
            else:
                transacoes.append (['Saldo', saldo])
                formatar (transacoes, { 'col1_size': 3, 'col2_size': 26, 'col3_size': 5, 'col4_size': 16})
                print ('-' * 60)

    elif opcao == '4':
        break
    
    else:
        print ('Operação inválida, por favor selecione novamente a opção desejada!')