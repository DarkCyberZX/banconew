from random import randint
from utils.helpers import menu_transacoes


class Conta:
    def criar_conta(self):
        print("Bem-vindo ao banco WordsCity\n"
              "Vamos criar sua conta neste momento.")
        conta_info = []
        agencia = "3186"
        numero_conta = str(randint(100000, 999999)) + "-9"
        nome_cliente = input("Digite seu nome completo: \n").title()
        senha = input("Digite sua senha: \n")
        saldo_inicial = randint(0, 5000)
        conta_info.extend([agencia, numero_conta, nome_cliente, senha, saldo_inicial])
        print(f"Parabéns {nome_cliente}, sua conta foi criada!\n"
              f"Agência: {agencia}\n"
              f"Número da conta: {numero_conta}\n"
              "Por favor, anote e não se esqueça.")
        return conta_info

    @staticmethod
    def acessar_conta(dados_usuarios):
        print("Para realizar transações bancárias, é necessário fazer login.")
        agencia = input("Digite sua agência: \n")
        numero_conta = input("Digite o número da sua conta: \n")
        senha = input("Digite sua senha: \n")

        for index, usuario in enumerate(dados_usuarios):
            if (agencia == usuario[0] and numero_conta == usuario[1] and senha == usuario[3]):
                print(f"Login realizado com sucesso! Bem-vindo, {usuario[2]}.\n")
                menu_transacoes(dados_usuarios, index)
                return

        print("Dados incorretos. Tente novamente.")
        Conta.acessar_conta(dados_usuarios)
