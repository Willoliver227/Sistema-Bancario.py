print("Bem vindo")

menu = """
Qual operação deseja realizar ?

[1] Deposito
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = 0

while True:
    opcao = input(menu)
    
    if opcao == "1":
        print("Deposito")
        valor = float(input("Qual valor deseja depositar ? "))
        if valor > 0:
            saldo += valor
            print("Valor depositado")
            depositos += 1
            
        
    elif opcao == "2":
        print("Sacar")
        valor = float(input("qual valor deseja sacar ?"))
        if valor > limite:
            print("Valor limite execedido, operação fracassada")
            
        elif valor > saldo:
            print("Saldo insuficiente, operação fracassada")
            
        elif numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            print ("Valor sacado")
        else:
            print("Numero de saques diario excedidos, operaação fracassada")
            break
            
    elif opcao == "3":
        print("=========Extrato=========")
        print(f"Depositos realizados:" , depositos)
        print(f"Saques realizados: " , numero_saques)
        print("Saldo R$ %.2f" % saldo)
        print("=========================")
        
    elif opcao == "4":
        print("Saindo do sistema")
        break