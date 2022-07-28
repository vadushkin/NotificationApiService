from django.test import TestCase
from ..models import *


class ApiModelsTests(TestCase):
    """Тесты"""
    @classmethod
    def setUpClass(cls):
        """Проверка рассылки"""
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
        cls.mailing = Mailing.objects.create(
            start_datetime='2022-03-15 13:10:10.294903',
            text='Проверка вывода текста в __str__',
            finish_datetime='2022-03-14 13:10:10.294903',
        )

    def test_models_client(self):
        """Проверяет модель 'Client'"""
        client = ApiModelsTests.client
        object_name = client.tag
        self.assertEqual(object_name, client.tag)

    def test_phone_client(self):
        """Проверяет модель 'Client'"""
        phone1 = ApiModelsTests.client.phone_number
        phone2 = self.client.phone_number = '79222222222'
        self.assertNotEqual(phone1, phone2)

    def test_str_mailing(self):
        """Проверяет модель 'Mailing'"""
        mailing = ApiModelsTests.mailing
        expected_object_name = mailing.text[:15]
        self.assertEqual(expected_object_name, str(mailing))
