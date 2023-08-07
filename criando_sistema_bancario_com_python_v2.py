from operator import itemgetter
from pyUFbr.baseuf import ufbr
import re
from rich.console import Console
import textwrap

c = Console ()

def menu ():
    c.rule ("MENU")
    menu = '''

    [1] Cadastrar Cliente
    [2] Cadastrar Conta Corrente
    [3] Verificar Cliente
    [4] Depositar
    [5] Sacar
    [6] Saldo (Tela)
    [7] Extrato
    [8] Sair

    => '''
    return input (menu)

#tentativa de criar cadastro com verificação de cfp e um menu bonito para selecionar estado e cidade,
#funciona fora da função, mas não dentro, tentei achar a solução durante 4 semanas, mas não consegui

# def cadastrar_cliente (usuarios):
    # cpf = str (input ('Digite o CPF (somente números): '))
    # numero = cpf.isdigit ()
    # formatacao = False
    # quant_digitos = False
    # select = ''
    # select2 = ''
    # estados = []
    # cidades = []
    # estado = []
    # cidade = []
    # state = []
    # city = []

    # #Retira traços e pontos da estrutura do CPF (11122233344)
    # cpf = re.sub (r'[^\w\s]','',cpf)
    # if numero == True and len (cpf) == 11:
    #     formatacao = True
    #     quant_digitos = True
    # else:
    #     print ('cpf invalido')
    
    # if quant_digitos == True and formatacao == True:
    #     if cpf in usuarios:
    #         print ('Usuário já cadastrado!')
    #         return
        
    #     nome = input ('Digite o nome completo: ')
    #     print ('Informe a data de nascimento (dd/mm/aaaa):')
    #     dia = input ('Dia: ')
    #     mes = input ('Mês: ')
    #     ano = input ('Ano: ')
    #     nascimento = (f'{dia}/{mes}/{ano}')  

    #     def selecionar_estado (estados, cols_sizes):
    #         estados = ufbr.list_uf
    #         col1_size = itemgetter ('col1_size')(cols_sizes)
    #         c.rule ("ESTADOS")
    #         for i, estado in enumerate (estados, start=1):
    #             print (f'[{i:02}] {estado:<{col1_size}}', end="")
    #             if i % 15 == 13:
    #                 print ("\n")
    #         print ("\n")
    #         c.rule ('')
    #         return ''
        
    #     selecao = input (f'Selecione o Estado: {selecionar_estado (estado, {"col1_size": 7, "col2_size": 10})}') 

    #     def selecionar_cidade (cidades, cols_sizes, select):
    #         estados = ufbr.list_uf
    #         for i, estado in enumerate (estados, start=1):
    #             if i == int (selecao):
    #                 select = (f'{estado}')
    #                 state.append (f'{estado}')

    #         cidades = ufbr.list_cidades (sigla = str (select))
    #         col1_size = itemgetter ('col1_size')(cols_sizes)    
    #         c.rule ("CIDADES")
    #         for i, cidade in enumerate (cidades, start=1):
    #             print (f'[{i:03}] {cidade:<{col1_size}}', end="")
    #             if i % 6 == 5:
    #                 print ("\n")
    #         print ("\n")
    #         c.rule ('')
    #         return ''

    #     selecao2 = input (f'Selecione a Cidade: {selecionar_cidade (cidade, {"col1_size": 27, "col2_size": 60}, select)}')
        
    #     state2 = str (state).strip ('['']').strip ("''")
        
    #     cities = ufbr.list_cidades (sigla = str (state2))
    #     for i, city in enumerate (cities, start=1):
    #         if i == int (selecao2):
    #             select = (f'{city}')
    #             cidade.append (f'{city}')

    #     city2 = str (cidade).strip ('['']').strip ("''")
    #     rua = input ('Digite o nome da rua: ')
    #     numero_casa = str (input ('Digite e numero: '))
    #     complemento = input ('Digite o complemento se tiver: ')
    #     bairro = input ('Digite o bairro: ')

    # usuarios.append ({'cpf': cpf, 'nome': nome, 'data_nascimento': nascimento, 'endereco' : [rua, numero_casa, complemento, bairro, city2, state2]})
    
    # print ('Cliente Cadastrado com sucesso!')

def cadastrar_cliente (usuarios):
    cpf = str (input ('Digite o CPF (somente números): '))
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print ('Usuário já cadastrado!')
        return
    
    nome = input ('Digite o nome completo: ')
    print ('Informe a data de nascimento (dd/mm/aaaa):')
    dia = input ('Dia: ')
    mes = input ('Mês: ')
    ano = input ('Ano: ')
    nascimento = (f'{dia}/{mes}/{ano}')
    endereco = input ('Insira o endereço completo (Rua, numero - bairro - cidade / Estado): ')

    usuarios.append ({'cpf': cpf, 'nome': nome, 'data_nascimento': nascimento, 'endereco' : endereco})

    print ('Cliente Cadastrado com sucesso!')

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None

def cadastrar_conta (agencia, numero_conta, usuarios):
    cpf = str (input ('Digite o CPF (somente números): '))
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print ('Conta Cadastrada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print ('Realize o cadastro do Cliente!')

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        extrato.append (['Depósito', valor])
        saldo += valor
        print ('Depósito Efetuado')
    else:
        print ('Por favor informe um valor válido!')

    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques > limite_saques:
        print (f'Você já atingiu o limite máximo de {limite_saques} saques permitidos por dia')
    elif valor < 0:
        print ('Por favor informe um valor válido!')
    elif valor > limite:
        print (f'Por favor insira um valor válido dentro do seu limite diário de R$ {limite:,.2f}')
    elif saldo >= valor:
        extrato.append (['Saque', valor])
        saldo -= valor
        numero_saques += 1
        print (f'Realizado saque de R$ {valor:,.2f}')
    else:
        print ('Você não tem saldo suficiente para realizar essa operação.')    

    return saldo, extrato

def consultar_conta (contas_correntes):
    for conta_corrente in contas_correntes:
        linha = f'''\
            Agência:\t {conta_corrente ["agencia"]}
            C/C:\t\t {conta_corrente ["numero_conta"]}
            Titular:\t {conta_corrente ["usuario"]["nome"]}
        '''
        print ('=' * 100)
        print (textwrap.dedent (linha))

def consultar_saldo (saldo):
    print (f'Seu saldo atual é de R$ {saldo:,.2f}')

def exibir_extrato (saldo, extrato):
    def formatar (extrato, cols_sizes):
        col1_size, col2_size, col3_size, col4_size = itemgetter ('col1_size', 'col2_size', 'col3_size', 'col4_size')(cols_sizes)
        print (f'{"EXTRATO":^60}')
        print ('-' * 60)
        print (f'{"Nr.":{col1_size}} {"TRANSAÇÃO":<{col2_size}} {"VALOR":>{col4_size}}')
        print ('-' * 60)
        for i, transacao in enumerate (extrato, start=1):             
            print (f'{i:>{col1_size}} {transacao [0]:<{col2_size}} {"R$":>{col3_size}} {transacao [1]:>{col4_size - 3},.2f}')

    if len (extrato) == 0:
        formatar (extrato, { 'col1_size': 3, 'col2_size': 26, 'col3_size': 5, 'col4_size': 16})
        print (f'{"NÃO HOUVE MOVIMENTAÇÃO NA CONTA":^60}')
        print ('-' * 60)
    else:
        extrato.append (['Saldo', saldo])
        formatar (extrato, { 'col1_size': 3, 'col2_size': 26, 'col3_size': 5, 'col4_size': 16})
        print ('-' * 60)

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas_correntes = []

    while True:
        opcao = menu ()

        if opcao == '1':
            cadastrar_cliente (usuarios)

        elif opcao == '2':
            numero_conta = len (contas_correntes) + 1
            conta = cadastrar_conta (AGENCIA, numero_conta, usuarios)

            if conta:
                contas_correntes.append (conta)

        elif opcao == '3':
            consultar_conta (contas_correntes)

        elif opcao == '4':
            valor = float (input ('Por favor insira o valor do Depósito: R$ '))
            saldo, extrato = depositar (saldo, valor, extrato)
        
        elif opcao == '5':
            valor = float (input ('Por favor insira o valor do Saque: R$ '))

            saldo, extrato = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        
        elif opcao == '6':
            consultar_saldo (saldo)
        
        elif opcao == '7':
            exibir_extrato (saldo, extrato)

        elif opcao == '8':
            break
        
        else:
            print ('Operação inválida, por favor selecione novamente a opção desejada!')

main ()