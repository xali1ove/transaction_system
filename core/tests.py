from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .models import Client
from rest_framework.test import APIRequestFactory,APITestCase


# Create your tests here.
class RegistrationTestCase(APITestCase):
    def setUp(self) -> None:
        self.registration_url = reverse('client-register')

    def test_positive_balance(self):
        client = Client.objects.create(username='testusername', password='testregistration')
        change_balance_url = reverse('client-change-balance', args=[client.id])

        self.client.force_login(client)
        data = {
            'change_balance_value': 100
        }

        response = self.client.post(change_balance_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_registration(self):
        data = {
            'username': 'testusername',
            'password': 'testregiration',
        }

        response = self.client.post(self.registration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_with_balance(self):
        data = {
            'username': 'testusername',
            'password': 'testregiration',
            'balance_value': 777.777
        }

        response = self.client.post(self.registration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
