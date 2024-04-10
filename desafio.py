# Variavel menu irá armazenar uma string, com as opcoes disponiveis no caixa eletronico
# Cada uma representada por uma letra e um verbo.
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variaveis
saldo = 0           # armazena o saldo atual da conta
limite = 500        # define o limite de saque diário
extrato = ""        # armazena o historico de transações
numero_saques = 0   # contador para registrar o numero de saques realizados no dia
LIMITE_SAQUES = 3   # limite de saques diários permitidos

# Loop -> fica em execução enquanto TRUE 
# Cada iteração, o usuário é solicitado a inserir uma opção do menu
# Variavel -> opcao: armazena a letra escolhida
while True:

    # Funcionalidades Implementadas:
        # Menu - Depósito - Saque - Extrato - sair
    # Funcionalidades Faltantes:
        # Validação de entrada
        # Implementação das funcionalidades de depósito e saque
        # Atualização do extrato
        # Limites de saque
    
    opcao = input(menu)     

    # Se o usuario digitar "d" o valor do deposito é solicitado
    # Se o valor for positivo, ele é adicionado ao saldo e registrado no extrato
    # Caso contrario uma mensagem de erro é exibida
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
	
    # Se o usuario digitar "s" o valor do saque é solicitado 
    # O valor é comparado com o saldo, o limite de saque e o numero de saques realizados
    # Se o valor for positivo e atender a todas as condições, ele é subtraido do saldo
    # Registrado no extrato e o numero de saques é incrementado 
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    # Se o usuario digitar "e" o extrato é exibido , mostrando as transações realizadas e o saldo atual 
    elif opcao == "e":
        print("\n========== ETRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("==============================")

    
    # Se o usuario digitar "q" o loop é encerrado e o programa termina
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
