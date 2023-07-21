menu = """
 Selecione a opção desejada:

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3   
soma_saque = 0


while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor do seu depósito? R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"
            print("\n Operação realizada com sucesso. Deseja algo mais?")

        else:
            print("\n Não foi possível efetuar sua operação: O valor informado é inválido.\n")
            print("Deseja algo mais?")

    elif opcao == "2":
        valor = float(input("\n Por favor, qual o valor que deseja sacar? "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        
        if excedeu_saldo:
            print("\n Sua operação não foi realizada: Você não possui saldo suficiente.\n")
            print(" Deseja algo mais?")

        elif excedeu_limite:
            print ("\n Sua operação não foi realizada: Limite de saque diário indisponível, seu limite de saque disponível no momento é: R$ 500,00")
            
        elif excedeu_saques:
            print (f"\n Sua operação não foi realizada: Números de saques disponíves atingido. Seu limite é de {LIMITE_SAQUES} saques.")
        
        elif valor > 0:
            saldo -= valor
            print("\n Saque realizado com sucesso.")
            print(f"\n Seu saldo dispinível é R$ {saldo:.2f}")
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1
            soma_saque += valor
            
        
        else:
            print("\n Operação não realizada: O valor informado não é válido\n")
            print("Deseja algo mais?")
    elif opcao == "3":
        print("\n ========== EXTRATO ==========\n")
        print("Não foram relizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n =============================")

    elif opcao == "0":
        print("Obrigado por usar nossos serviços.")
        break

    else: 
        print("\n Opção inválida, por favor selecione uma das opções válicas e tente novamente.")
