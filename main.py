from models.conta import Conta

def main():
    dados_usuarios = []
    while True:
        print("Bem-vindo ao Banco WordsCity!\n"
              "1 - Criar nova conta\n"
              "2 - Acessar conta existente\n"
              "3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_conta = Conta()
            dados_usuarios.append(nova_conta.criar_conta())
        elif opcao == "2":
            if not dados_usuarios:
                print("Nenhuma conta registrada. Crie uma nova conta antes de acessar.")
            else:
                Conta.acessar_conta(dados_usuarios)
        elif opcao == "3":
            print("Obrigado por utilizar o Banco WordsCity! Até logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
