import unittest
from unittest.mock import patch
from utils.helpers import (
    realizar_deposito,
    realizar_saque,
    realizar_transferencia,
    menu_transacoes,
)

class TestHelpers(unittest.TestCase):
    def setUp(self):
        """
        Configura os dados iniciais para os testes.
        """
        self.dados_usuarios = [
            ["3186", "123456-9", "Maria Silva", "senha123", 1000.00],
            ["3186", "654321-9", "João Pereira", "senha456", 2000.00],
        ]

    @patch("builtins.input", return_value="500")
    def test_realizar_deposito(self, mock_input):
        """
        Testa o depósito de valores.
        """
        realizar_deposito(self.dados_usuarios, 0)  # Maria deposita 500
        self.assertEqual(self.dados_usuarios[0][4], 1500.00)  # Saldo deve ser atualizado

    @patch("builtins.input", return_value="200")
    def test_realizar_saque(self, mock_input):
        """
        Testa o saque de valores.
        """
        realizar_saque(self.dados_usuarios, 1)  # João saca 200
        self.assertEqual(self.dados_usuarios[1][4], 1800.00)  # Saldo deve ser atualizado

    @patch("builtins.input", side_effect=["3186", "123456-9", "300"])
    def test_realizar_transferencia(self, mock_input):
        """
        Testa a transferência entre contas.
        """
        realizar_transferencia(self.dados_usuarios, 1)  # João transfere 300 para Maria
        self.assertEqual(self.dados_usuarios[1][4], 1700.00)  # João: Saldo reduzido
        self.assertEqual(self.dados_usuarios[0][4], 1300.00)  # Maria: Saldo aumentado

    @patch("builtins.input", side_effect=["4"])  # Simula a opção de logout
    def test_menu_transacoes_logout(self, mock_input):
        """
        Testa a opção de logout no menu de transações.
        """
        menu_transacoes(self.dados_usuarios, 0)

    @patch("builtins.input", return_value="5")  # Opção de sair
    def test_menu_transacoes_sair(self, mock_input):
        """
        Testa a opção de sair no menu de transações.
        """
        with self.assertRaises(SystemExit):  # O programa é encerrado
            menu_transacoes(self.dados_usuarios, 0)


if __name__ == "__main__":
    unittest.main()
