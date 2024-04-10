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

    if opcao == "d":
        print("Depósito")
	
    elif opcao == "s":
        input("Saque")

    elif opcao == "e":
        print("Extrato")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
