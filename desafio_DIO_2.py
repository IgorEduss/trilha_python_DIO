# OTIMIZANDO O SISTEMA BANCARIO COM FUNCOES PYTHON

menu = """
==============================   MENU  =============================
                        [d] - Depositar
                        [s] - Sacar
                        [e] - Extrato
                        [q] - Sair
                        [c] - Criar conta
                        [lc] - Listar contas
===================================================================
"""

login = """
{}

{}

{}
{}

{}
{}

{}
{}
""".format(' LOGIN '.center(100, '='),
           ' SEJA BEM VINDO AO BANCO DIO '.center(100, ' '),
           ' SE JÁ FOR NOSSO CLIENTE, ENTRE DIGITANDO SEU CPF '.ljust(100, ' '),
           ' SE AINDA NÃO É NOSSO CLIENTE, NÃO PERCA TEMPO E JUNTE-SE A NÓS! ;) '.ljust(100, ' '),
           ' [cpf] - Login '.ljust(100, ' '),
           ' [u]- Cadastrar usuário '.ljust(100, ' '),
           ' [q]- Sair '.ljust(100, ' '),
           ''.center(100, '=')
           )



def fazer_login(cpf, contas:list[dict]):
    login = False
    usuario_ativo = None
    for conta in contas:
        if cpf == conta['cpf']:
            print(f'Seja bem vindo, {conta["nome"]}')
            login, usuario_ativo = True, cpf
            return (login, usuario_ativo,)
    else:
        print('CPF nao encontrado.\nPor favor, crie sua conta com a gente! ;)')
        return None

def depositar(saldo, valor, extrato,/):
    if valor < 0:
        print('Deposite um valor válido.')
    saldo +=  valor
    extrato+= f'\nDepósito: R$ {valor:.2f}\n'
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, nro_saque, lmt_saques,):
    if valor > limite:
        print('Saque não autorizado. Limite máximo por operação é de R$ 500,00')
    elif saldo == 0:
        print('Saque não autorizado. Seu saldo está zerado.')
    elif valor > saldo:
        print('Saque não autorizado. Valor de saque superior ao disponível no seu saldo.')
    elif nro_saque > lmt_saques:
        print('Saque não autorizado. Limite de número de saques excedido.')
    else:
        print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        nro_saque +=1
        extrato+= f'\nsaque: R$ -{saque:.2f}\n'
        saldo -= saque
    return saldo, extrato, nro_saque

def tirar_extrato(saldo,/,*,extrato):
    if extrato == "":
        print('Conta sem movimentação bancária')
        return
    print('Extrato'.center(40, '-'))
    print(f'{extrato}')
    print(f'Saldo em conta: R$ {saldo:.2f}')
    print(''.center(40, '-'))

def criar_usuario(nome, data_nascimento, cpf, endereco):
    usuario = {'nome': nome,
           'data_de_nascimenot': data_nascimento,
           'cpf': cpf,
           'endereco':endereco
           }
    return usuario

def cadastro_usuario():

    nome = input('Por favor, digite o nome: ').strip()
    while True:
        print('Por favor, didite a data de nascimento. \nA data de nascimento deve ter o formato (DD/MM/AAAA)')
        dn  = input('Data de nascimento: ')
        if (dn.count('/') !=2) or (len(dn.replace('/', '')) != 8) or (dn.replace('/', '').isnumeric == False):
            print('Data de nascimento inválida, repetindo o processo...')
            continue
        else:
            print('Data de nascimento cadastrada com sucesso!')
            break
        
    while True:
        print('Por favor, didite o CPF. \nO CPF deve conter apenas os 11 dígitos numéricos')
        cpf = input(f'CPF do {nome}: ')
        if cpf.isnumeric and len(cpf)==11:
            print('CPF cadastrado com sucesso.')
            break
        else:
            print('CPF inválido, repetindo o processo...')
    while True:
        print('Por favor, digite o endereco. \nO endereco deve ser composta por logradouro, número, bairro, cidade/sigla estado')
        print()
        logradouro = input(f'Logradouro: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade_estado = input('Cidade/estado: ')

        endereco = {'logradouro': logradouro,
                    'numero': numero,
                    'bairro': bairro,
                    'cidade/estado': cidade_estado
                    }
        confirmacao = input('Confirma o endereço? [S/N]').upper().strip()
        if confirmacao == 'S':
            print('Endereço cadastrado com sucesso.')
            break
        else:
            print('Repetindo o processo...\n')
            continue
    return nome, dn, cpf, endereco

def criar_conta(cpf, nro_conta, agencia = '0001'):

    conta = {'agencia': agencia,
             'numero_conta': nro_conta, 
             'usuario': cpf}
    nro_conta+=1
    return conta, nro_conta

def cadastro_conta():
    while True:
        print('Por favor, um CPF de usuário previamente cadastrado. \nO CPF deve conter apenas os 11 dígitos numéricos\n')
        cpf = input(f'CPF: ')
        if cpf.isnumeric and len(cpf)==11:
            for conta in usuarios:
                if cpf == conta['cpf']:
                    print(f'\nCPF válido. Criando conta para {conta["nome"]}.')
                    break
            return cpf
        else:
            print('\nCPF inválido, repetindo o processo...')

def listar_contas(contas):
    for conta in contas:
        for chave, valor in conta.items():
            print(chave,':', valor)
        print( '-='*30)

def sair():
    print('\nObirgado por usar nossos serviços bancários. Volte sempre!')

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 1
inicio = False
fim = None
usuario_ativo = None
novo = None


while True:
    if inicio == False:
        while True:
            comeco = input(login)
            if comeco == 'cpf':
                cpf = input('Digite o cpf cadastrado: ')
                if cpf.isnumeric and len(cpf)==11:
                    lg = fazer_login(cpf, contas=contas)
                    if lg != None:
                        login, usuario_ativo = lg
                        inicio = True
                        break
                    else:
                        continue
            elif comeco == 'q':
                fim = comeco
                break
            elif comeco != 'cpf' and comeco != 'u' and comeco != 'q':
                print('Selecione uma opcao válida...')
                continue
            else:
                while True:
                    cadastro = cadastro_usuario()
                    usuario = criar_usuario(*cadastro)
                    usuarios.append(usuario)
                    usuario_ativo = usuario['cpf']
                    inicio = True
                    while True:
                        de_novo = input('Cadastrar novo  usuario? [s/n]').lower()
                        if de_novo == 's':
                            novo = True
                            break
                        elif de_novo == 'n':
                            novo = False
                            break
                        else:
                            print('Digite uma das opcoes possiveis...')
                            continue
                    if novo:
                        continue
                    else:
                        break
                break

    if fim == 'q': # sair
        sair()
        break

    opcao = input(menu)
    
    if opcao.lower() == "d".lower(): # depositar
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao.lower() == "s": #sacar
        saque = float(input(f"Digite o valor a ser sacado: R$"))
        saldo, extrato, numero_saques = sacar(saldo = saldo, valor = saque, extrato= extrato, limite = limite, nro_saque=numero_saques, lmt_saques=LIMITE_SAQUES)
    
    elif opcao.lower() == "e": # extrato
        tirar_extrato(saldo, extrato=extrato)

    elif opcao.lower() == "q" or fim == 'fim': # sair
        sair()
        break

    elif opcao.lower() == "c": # cria conta
        cpf= cadastro_conta()
        conta, numero_conta = criar_conta(cpf, nro_conta = numero_conta)
        contas.append(conta)
        
    elif opcao.lower() == "lc": # listar contas
        listar_contas(contas)
        
    else:
        print("Operação inválida, porfavor selecione um comando válido.")


