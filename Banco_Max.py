menu = """
         \033[1;33mBANCO MAX\033[m
=============================
     [d] Depositar
     [s] Sacar
     [e] Extrato
     [q] sair
-----------------------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor do depósito: "))
        print('~'*32)
        print(f"\033[1;32mR${valor} Depositado com sucesso!\033[m")
        print('~'*32)
        if valor >0:
            saldo +=valor
            extrato += f"Depósito de R$ {valor:.2f}.\n"
        else:
            print("\033[1;31mA operação falhou!\033[m O valor informado não pode ser negativo!")

    elif opção == "s":
        valor = float(input("Informe o quanto você quer sacar: "))
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque
        print(f'\033[1;34mR${valor} Retirado com sucesso!\033[m')
        if excedeu_saldo:
            print('\033[1;31mVocê não tem saldo o suficiente!\033[m')
        elif excedeu_limite:
            print("\033[1;31mO valor do saque excede o limite de R$500!\033[m")
        elif excedeu_saques:
            print('\033[1;31mNúmero máximo de saque (3) excedido!\033[m')

        elif valor >0:
            saldo-=valor
            extrato += f"Saque: R${valor:.2f}.\n"
            numero_saque +=1

        else:
            print('\033[1;31mOperação falhou!\033[m O valor informado é inválido!')
    
    elif opção == "e":
        print("\n\033[1;36m==========extrato============\033[m")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('\033[1;36m=============================\033[m')

    elif opção == "q":
        break
    
    else:
        print('\033[1;31mOpção inválida!\033[m Selecione novamente a opção desejada!')

print('\033[1;35mObrigada! ^^\033[m')