def exibir_menu_transacoes(dados_usuarios, indice_usuario):
    """
    Exibe o menu de transações e retorna a opção escolhida pelo usuário.
    """
    print(f"\nSeu saldo atual é: R${float(dados_usuarios[indice_usuario][4]):.2f}\n"
          "Escolha uma operação:\n"
          "1 - Depósito\n"
          "2 - Saque\n"
          "3 - Transferência\n"
          "4 - Logout\n"
          "5 - Sair")
    return input("Digite a opção desejada: ")


def realizar_deposito(dados_usuarios, indice_usuario):
    """
    Realiza um depósito no saldo do usuário.
    """
    try:
        valor_deposito = float(input("Qual valor deseja depositar? \n"))
        if valor_deposito > 0:
            dados_usuarios[indice_usuario][4] += valor_deposito
            print(f"Depósito realizado com sucesso! Saldo atual: R${dados_usuarios[indice_usuario][4]:.2f}")
        else:
            print("O valor de depósito deve ser positivo.")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def realizar_saque(dados_usuarios, indice_usuario):
    """
    Realiza um saque do saldo do usuário.
    """
    try:
        valor_saque = float(input("Qual valor deseja sacar? \n"))
        if valor_saque > 0 and valor_saque <= dados_usuarios[indice_usuario][4]:
            dados_usuarios[indice_usuario][4] -= valor_saque
            print(f"Saque realizado com sucesso! Saldo atual: R${dados_usuarios[indice_usuario][4]:.2f}")
        elif valor_saque > dados_usuarios[indice_usuario][4]:
            print("Saldo insuficiente.")
        else:
            print("O valor de saque deve ser positivo.")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def realizar_transferencia(dados_usuarios, indice_usuario):
    """
    Realiza uma transferência entre contas.
    """
    agencia_destino = input("Digite a agência de destino: \n")
    conta_destino = input("Digite o número da conta de destino: \n")
    try:
        valor_transferencia = float(input("Qual valor deseja transferir? \n"))
        if valor_transferencia > 0 and valor_transferencia <= dados_usuarios[indice_usuario][4]:
            for usuario in dados_usuarios:
                if usuario[0] == agencia_destino and usuario[1] == conta_destino:
                    dados_usuarios[indice_usuario][4] -= valor_transferencia
                    usuario[4] += valor_transferencia
                    print(f"Transferência realizada com sucesso! Saldo atual: R${dados_usuarios[indice_usuario][4]:.2f}")
                    return
            print("Conta de destino não encontrada.")
        elif valor_transferencia > dados_usuarios[indice_usuario][4]:
            print("Saldo insuficiente.")
        else:
            print("O valor de transferência deve ser positivo.")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def menu_transacoes(dados_usuarios, indice_usuario):
    """
    Exibe o menu de transações e executa as operações escolhidas pelo usuário.
    """
    while True:
        opcao = exibir_menu_transacoes(dados_usuarios, indice_usuario)

        if opcao == "1":
            realizar_deposito(dados_usuarios, indice_usuario)
        elif opcao == "2":
            realizar_saque(dados_usuarios, indice_usuario)
        elif opcao == "3":
            realizar_transferencia(dados_usuarios, indice_usuario)
        elif opcao == "4":
            print("Logout realizado com sucesso!")
            break  # Sai do loop para voltar ao programa principal
        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
            exit() 
        else:
            print("Opção inválida. Tente novamente.")
    return True  # Retorna True para continuar no programa


# Exemplo de uso do programa principal
if __name__ == "__main__":
    # Dados fictícios dos usuários
    dados_usuarios = [
        ["3186", "123456-7", "Maria Silva", "senha123", 1000.0],
        ["3186", "765432-1", "João Pereira", "senha456", 2000.0],
    ]
    indice_usuario = 0  # Suponha que o primeiro usuário está logado
    
    print("Bem-vindo ao banco WordsCity!")
    continuar = True
    while continuar:
        continuar = menu_transacoes(dados_usuarios, indice_usuario)
