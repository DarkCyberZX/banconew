import sys

"""
Este módulo contém funções auxiliares para operações bancárias,
como depósito, saque e transferência de valores.
"""

def exibir_menu_transacoes(usuarios, indice):
    """
    Exibe o menu de transações e retorna a opção escolhida pelo usuário.
    """
    print(f"\nSeu saldo atual é: R${float(usuarios[indice][4]):.2f}\n"
          "Escolha uma operação:\n"
          "1 - Depósito\n"
          "2 - Saque\n"
          "3 - Transferência\n"
          "4 - Logout\n"
          "5 - Sair")
    return input("Digite a opção desejada: ")


def realizar_deposito(usuarios, indice):
    """
    Realiza um depósito no saldo do usuário.
    """
    try:
        valor_deposito = float(input("Qual valor deseja depositar? \n"))
        if valor_deposito > 0:
            usuarios[indice][4] += valor_deposito
            print(f"Depósito realizado com sucesso! Saldo atual: R${usuarios[indice][4]:.2f}")
        else:
            print("O valor de depósito deve ser positivo.")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def realizar_saque(usuarios, indice):
    """
    Realiza um saque do saldo do usuário.
    """
    try:
        valor_saque = float(input("Qual valor deseja sacar? \n"))
        if 0 < valor_saque <= usuarios[indice][4]:
            usuarios[indice][4] -= valor_saque
            print(f"Saque realizado com sucesso! Saldo atual: R${usuarios[indice][4]:.2f}")
        elif valor_saque > usuarios[indice][4]:
            print("Saldo insuficiente.")
        else:
            print("O valor de saque deve ser positivo.")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def realizar_transferencia(usuarios, indice):
    """
    Realiza uma transferência entre contas.
    """
    agencia_destino = input("Digite a agência de destino: \n")
    conta_destino = input("Digite o número da conta de destino: \n")
    try:
        valor_transferencia = float(input("Qual valor deseja transferir? \n"))
        if 0 < valor_transferencia <= usuarios[indice][4]:
            for usuario in usuarios:
                if usuario[0] == agencia_destino and usuario[1] == conta_destino:
                    usuarios[indice][4] -= valor_transferencia
                    usuario[4] += valor_transferencia
                    print(f"Transferência realizada! Saldo atual: R${usuarios[indice][4]:.2f}")
                    return
            print("Conta de destino não encontrada.")
        elif valor_transferencia > usuarios[indice][4]:
            print("Saldo insuficiente.")
        else:
            print("O valor de transferência deve ser positivo.")
    except ValueError:
        print("Valor inválido. Tente novamente.")


def menu_transacoes(usuarios, indice):
    """
    Exibe o menu de transações e executa as operações escolhidas pelo usuário.
    """
    while True:
        opcao = exibir_menu_transacoes(usuarios, indice)

        if opcao == "1":
            realizar_deposito(usuarios, indice)
        elif opcao == "2":
            realizar_saque(usuarios, indice)
        elif opcao == "3":
            realizar_transferencia(usuarios, indice)
        elif opcao == "4":
            print("Logout realizado com sucesso!")
            break  # Sai do loop para voltar ao programa principal
        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
            sys.exit()  # Usando sys.exit() ao invés de exit()
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
    INDICE_USUARIO = 0  # Constante para o índice do usuário logado
    print("Bem-vindo ao banco WordsCity!")
    CONTINUAR = True  # Usando maiúsculas para constantes
    while CONTINUAR:
        CONTINUAR = menu_transacoes(dados_usuarios, INDICE_USUARIO)
