import unittest
from unittest.mock import patch
from models.conta import Conta

class TestConta(unittest.TestCase):

    @patch('builtins.input', side_effect=["João Silva", "senha123"])
    @patch('builtins.print')
    def test_criar_conta(self, mock_print, mock_input):
        conta = Conta()
        conta_dados = conta.criar_conta()

        self.assertEqual(conta.nome_cliente, "João Silva")
        self.assertEqual(conta.agencia, "3186")

if __name__ == "__main__":
    unittest.main()
