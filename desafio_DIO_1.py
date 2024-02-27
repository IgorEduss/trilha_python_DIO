menu = """
==============================   MENU  =============================
                        [d] - Depositar
                        [s] - Sacar
                        [e] - Extrato
                        [q] - Sair
===================================================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.lower() == "d".lower(): # depositar
        deposito = float(input("Digite o valor a ser depositado: R$"))
        if deposito < 0:
            print('Deposite um valor válido.')
            continue
        saldo +=  deposito
        extrato+= f'\nDepósito: R$ {deposito:.2f}\n'
    
    elif opcao.lower() == "s": #sacar
        saque = float(input(f"Digite o valor a ser sacado: R$"))

        if saque > 500.00:
            print('Saque não autorizado. Limite máximo por operação é de R$ 500,00')
            continue
        elif saldo == 0:
            print('Saque não autorizado. Seu saldo está zerado.')
            continue
        elif saque > saldo:
            print('Saque não autorizado. Valor de saque superior ao disponível no seu saldo.')
            continue
        elif numero_saques > LIMITE_SAQUES:
            print('Saque não autorizado. Limite de número de saques excedido.')
            continue
        else:
            print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
            numero_saques +=1
            extrato+= f'\nsaque: R$ -{saque:.2f}\n'
            saldo -= saque
    
    elif opcao.lower() == "e": # extrato
        if extrato == "":
            print('Conta sem movimentação bancária')
            continue
        print('Extrato'.center(40, '-'))
        print(f'{extrato}')
        print(f'Saldo em conta: R$ {saldo:.2f}')
        print(''.center(40, '-'))

    elif opcao.lower() == "q": # sair
        print('Obirgado por usar nossos serviços bancários. Volte sempre!')
        break
    else:
        print("Operação inválida, porfavor selecione um comando válido.")


