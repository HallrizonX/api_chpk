import json
import requests
from django.test import TestCase
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.test import APITestCase
from rest_framework import status as st

from .models import Profile
from .serializers import ProfileSerializers


class APIConnection(APITestCase):

    def create_token(self):
        response = requests.post(self.get_url(self.domain, self.create_toke_url), self.test_data)
        token = json.loads(response.content)['data']['token']
        return [response, token]

    def setUp(self) -> None:
        self.domain: str = 'http://127.0.0.1:8000'  # Local server
        self.create_toke_url: str = '/auth/jwt/create/'
        self.list_profiles_url: str = '/api/v1/profiles/'
        self.detail_profiles_url: str = '/api/v1/profiles/1/'
        self.list_teachers_file_url: str = '/api/v1/teachers/files/'
        self.detail_teachers_file_url: str = '/api/v1/teachers/files/1/'
        self.list_teachers_url: str = '/api/v1/teachers/'
        self.detail_teachers_url: str = '/api/v1/teachers/1/'

        self.list_groups_url: str = '/api/v1/groups/'
        self.detail_groups_url: str = '/api/v1/groups/1/'

        self.list_subjects_url: str = '/api/v1/subjects/'
        self.detail_subjects_url: str = '/api/v1/subjects/1/'

        self.test_data: dict = {
            "username": "admin",
            "password": "rombik99"
        }

    def test_list_profiles(self):
        _, token = self.create_token()

        # profile
        response = requests.get(self.get_url(self.domain, self.list_profiles_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        response = requests.get(self.get_url(self.domain, self.detail_profiles_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        # teachers
        response = requests.get(self.get_url(self.domain, self.list_teachers_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        response = requests.get(self.get_url(self.domain, self.detail_teachers_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        response = requests.get(self.get_url(self.domain, self.list_teachers_file_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        response = requests.get(self.get_url(self.domain, self.detail_teachers_file_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        # groups
        response = requests.get(self.get_url(self.domain, self.list_groups_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        response = requests.get(self.get_url(self.domain, self.detail_groups_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        # subjects
        response = requests.get(self.get_url(self.domain, self.list_subjects_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)
        response = requests.get(self.get_url(self.domain, self.detail_subjects_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def checkout(self, response):
        self.assertEqual(st.HTTP_200_OK, response.status_code)
        self.assertTrue('data' in str(json.loads(response.content)))
        self.assertTrue('result' in str(json.loads(response.content)))

    def get_url(self, domain, url) -> str:
        if domain.endswith('/'):
            domain = domain[:-1]
        return f"{domain}{url}"