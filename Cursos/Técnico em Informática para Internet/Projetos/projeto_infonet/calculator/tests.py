import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import Calculation
from .utils import safe_eval

class SafeEvalTestCase(TestCase):
    """Testes unitários para a função de parsing seguro de expressões matemáricas."""
    
    def test_basic_arithmetic(self):
        self.assertEqual(safe_eval("2 + 3"), 5)
        self.assertEqual(safe_eval("10 - 4"), 6)
        self.assertEqual(safe_eval("3 * 4"), 12)
        self.assertEqual(safe_eval("10 / 2"), 5)
        self.assertEqual(safe_eval("2 ^ 3"), 8)
        self.assertEqual(safe_eval("5 % 2"), 1)
        self.assertEqual(safe_eval("-5 + 10"), 5)

    def test_scientific_functions(self):
        self.assertEqual(safe_eval("sqrt(16)"), 4)
        # sin(30) = 0.5 em graus
        self.assertAlmostEqual(safe_eval("sin(30)"), 0.5)
        # cos(0) = 1
        self.assertEqual(safe_eval("cos(0)"), 1)
        # tan(45) = 1
        self.assertAlmostEqual(safe_eval("tan(45)"), 1)
        # exp(1) = e
        self.assertAlmostEqual(safe_eval("exp(1)"), 2.7182818284, places=6)
        # log(e) = 1
        self.assertEqual(safe_eval("log(e)"), 1)
        # log10(100) = 2
        self.assertEqual(safe_eval("log10(100)"), 2)

    def test_constants(self):
        self.assertAlmostEqual(safe_eval("pi"), 3.1415926535, places=6)
        self.assertAlmostEqual(safe_eval("e"), 2.7182818284, places=6)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_eval("5 / 0")

    def test_invalid_syntax(self):
        with self.assertRaises(ValueError):
            safe_eval("2 +")
        with self.assertRaises(ValueError):
            safe_eval("sin(")
        with self.assertRaises(TypeError):
            safe_eval("unknown_func(10)")

    def test_injection_prevention(self):
        # Tentativas de usar classes de sistema ou imports devem falhar
        with self.assertRaises(ValueError):
            safe_eval("__import__('os').system('ls')")
        with self.assertRaises(ValueError):
            safe_eval("eval('2+2')")


class CalculatorAPITestCase(TestCase):
    """Testes de integração para os endpoints REST da calculadora."""

    def setUp(self):
        self.client = Client()
        self.calculate_url = reverse('calculator:calculate')
        self.history_url = reverse('calculator:history')
        self.clear_url = reverse('calculator:clear_history')

    def test_calculate_endpoint_success(self):
        payload = {'expression': '10 * 5 + 2'}
        response = self.client.post(
            self.calculate_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['result'], '52')

        # Verificar se salvou no banco
        self.assertEqual(Calculation.objects.count(), 1)
        self.assertEqual(Calculation.objects.first().expression, '10 * 5 + 2')

    def test_calculate_endpoint_error(self):
        # Divisão por zero
        payload = {'expression': '10 / 0'}
        response = self.client.post(
            self.calculate_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('Divisão por zero', data['error'])

        # Sintaxe incorreta
        payload = {'expression': 'abc'}
        response = self.client.post(
            self.calculate_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_history_endpoint(self):
        # Criar alguns cálculos
        Calculation.objects.create(expression='2+2', result='4')
        Calculation.objects.create(expression='3*3', result='9')

        response = self.client.get(self.history_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        # Ordenação deve ser do mais recente para o mais antigo
        self.assertEqual(data[0]['expression'], '3*3')
        self.assertEqual(data[1]['expression'], '2+2')

    def test_clear_history_endpoint(self):
        Calculation.objects.create(expression='2+2', result='4')
        self.assertEqual(Calculation.objects.count(), 1)

        response = self.client.delete(self.clear_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        self.assertEqual(Calculation.objects.count(), 0)
