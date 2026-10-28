import sys
from io import StringIO
import unittest

sys.path.append("src")
from calculadora import somar, subtrair, multiplicar, dividir, porcentagem, main

class TestCalculadora(unittest.TestCase):
    def test_operacoes_basicas(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(dividir(10, 5), 2.0)

    def test_divisao_por_zero(self):
        self.assertEqual(dividir(10, 0), "Erro: Não é possível dividir por zero!")

    def test_porcentagem(self):
        self.assertEqual(porcentagem(200, 15), 30.0)
        self.assertEqual(porcentagem(50, 10), 5.0)
        self.assertEqual(porcentagem(100, 0), 0.0)
        self.assertEqual(porcentagem(0, 50), 0.0)

    def run_main_with_inputs(self, inputs):
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO("\n".join(inputs) + "\n")
        sys.stdout = StringIO()
        try:
            main()
            return sys.stdout.getvalue()
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    def test_main_porcentagem_fluxo(self):
        output = self.run_main_with_inputs(["200", "%", "15"])
        self.assertIn("Resultado: 200.0 % 15.0 = 30.0", output)

    def test_main_divisao_zero_fluxo(self):
        output = self.run_main_with_inputs(["10", "/", "0"])
        self.assertIn("Erro: Não é possível dividir por zero!", output)

    def test_main_operacao_invalida(self):
        output = self.run_main_with_inputs(["10", "x", "5"])
        self.assertIn("Operação inválida! Use apenas +, -, *, / ou %.", output)

    def test_main_entrada_invalida(self):
        output = self.run_main_with_inputs(["abc", "+", "5"])
        self.assertIn("Erro: Por favor, digite apenas números válidos!", output)

if __name__ == "__main__":
    unittest.main()

