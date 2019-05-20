import json
import requests
from rest_framework.test import APITestCase
from rest_framework import status as st


class ProfileJWT(APITestCase):
    def get_url(self, domain, url) -> str:
        if domain.endswith('/'):
            domain = domain[:-1]
        return f"{domain}{url}"

    def create_token(self):
        response = requests.post(self.get_url(self.domain, self.create_toke_url), self.test_data)
        token = json.loads(response.content)['data']['token']
        return [response, token]

    def setUp(self) -> None:
        self.domain: str = 'http://127.0.0.1:8000'
        self.create_toke_url: str = '/auth/jwt/create/'
        self.verify_token_url: str = '/auth/jwt/verify/'
        self.refresh_token_url: str = '/auth/jwt/refresh/'
        self.list_profiles_url: str = '/api/v1/profiles/'
        self.detail_profiles_url: str = '/api/v1/profiles/1/'

        self.test_data: dict = {
            "username": "admin",
            "password": "rombik99"
        }

    def test_create_and_verify_token(self):
        # Create token
        response, token = self.create_token()

        self.assertEqual(st.HTTP_200_OK, response.status_code)
        self.assertTrue('token' in str(json.loads(response.content)))

        # Verify token
        response = requests.post(self.get_url(self.domain, self.verify_token_url), {'token': token})
        self.assertEqual(st.HTTP_200_OK, response.status_code)

    def test_list_profiles(self):
        _, token = self.create_token()

        response = requests.get(self.get_url(self.domain, self.list_profiles_url),
                                headers={"Authorization": f"JWT {token}"})
        self.assertEqual(st.HTTP_200_OK, response.status_code)
        self.assertTrue('data' in str(json.loads(response.content)))
        self.assertTrue('result' in str(json.loads(response.content)))

    def test_detail_profile(self):
        _, token = self.create_token()

        response = requests.get(self.get_url(self.domain, self.detail_profiles_url),
                                headers={"Authorization": f"JWT {token}"})
        self.assertEqual(st.HTTP_200_OK, response.status_code)
        self.assertTrue('data' in str(json.loads(response.content)))
        self.assertTrue('result' in str(json.loads(response.content)))
