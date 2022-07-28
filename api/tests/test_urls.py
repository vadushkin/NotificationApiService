from django.test import TestCase

from ..models import *


class ApiURLTests(TestCase):
    """Тесты 2"""
    @classmethod
    def setUpClass(cls):
        """Проверка оператора мобильной связи"""
        super().setUpClass()
        cls.tag = Tag.objects.create(
            name='911'
        )
        cls.operator = Operator.objects.create(
            name='МТС'
        )
        cls.client = Client.objects.create(
            phone_number='79111111111',
            operator=cls.operator,
            tag=cls.tag,
        )

    def test_index_api(self):
        """Проверяет доступность страницы api/v1/"""
        response = self.client.get('http://127.0.0.1:8000/api/v1/')
        self.assertEqual(response.status_code, 200)

    def test_index_mailings(self):
        """Проверяет доступность страницы 'mailings'"""
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/mailings/')
        self.assertEqual(response.status_code, 200)

    def test_index_clients(self):
        """Проверяет доступность страницы 'clients'"""
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/clients/')
        self.assertEqual(response.status_code, 200)

    def test_index_messages(self):
        """Проверяет доступность страницы 'messages'"""
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/messages/')
        self.assertEqual(response.status_code, 200)

    def test_index_operators(self):
        """Проверяет доступность страницы 'operators'"""
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/operators/')
        self.assertEqual(response.status_code, 200)

    def test_index_tags(self):
        """Проверяет доступность страницы 'tags'"""
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/tags/')
        self.assertEqual(response.status_code, 200)
