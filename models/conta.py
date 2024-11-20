from random import randint
from utils.helpers import menu_transacoes
import re  # Para usar expressões regulares

class Conta:
    def __init__(self):
        self.agencia = "3186"
        self.numero_conta = f"{randint(100000, 999999)}-9"
        self.nome_cliente = ""
        self.senha = ""
        self.saldo_inicial = randint(0, 5000)

    def criar_conta(self):
        """Cria uma nova conta com dados do cliente."""
        print("Bem-vindo ao banco WordsCity\n"
              "Vamos criar sua conta neste momento.")
        
        tentativa = 0  # Contador de tentativas para nome válido
        while tentativa < 3:
            self.nome_cliente = input("Digite seu nome completo: \n").title()

            # Verificar se o nome contém apenas letras e espaços
            if re.match("^[A-Za-zÀ-ÿ ]+$", self.nome_cliente):
                break
            else:
                print("Nome inválido. O nome não pode conter números ou caracteres especiais. Tente novamente.")
                tentativa += 1
        else:
            print("Número de tentativas excedido. Retornando ao menu principal.")
            return

        self.senha = input("Digite sua senha: \n")
        print(f"Parabéns {self.nome_cliente}, sua conta foi criada!\n"
              f"Agência: {self.agencia}\n"
              f"Número da conta: {self.numero_conta}\n"
              "Por favor, anote e não se esqueça.")
        return [self.agencia, self.numero_conta, self.nome_cliente, self.senha, self.saldo_inicial]

    @staticmethod
    def acessar_conta(dados_usuarios):
        """Realiza o login e acessa as transações de uma conta existente."""
        print("Para realizar transações bancárias, é necessário fazer login.")
        tentativa = 0

        while tentativa < 3:  # Limite de 3 tentativas
            agencia = input("Digite sua agência: \n")
            numero_conta = input("Digite o número da sua conta: \n")
            senha = input("Digite sua senha: \n")

            for index, usuario in enumerate(dados_usuarios):
                if agencia == usuario[0] and numero_conta == usuario[1] and senha == usuario[3]:
                    print(f"Login realizado com sucesso! Bem-vindo, {usuario[2]}.\n")
                    menu_transacoes(dados_usuarios, index)
                    return

            print("Dados incorretos. Tente novamente.")
            tentativa += 1

        print("Número de tentativas excedido. Retornando ao menu principal.")
