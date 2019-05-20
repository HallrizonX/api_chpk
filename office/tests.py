import json
import requests
from rest_framework.test import APITestCase
from rest_framework import status as st


class APIConnection(APITestCase):

    def setUp(self) -> None:
        self.domain: str = 'http://127.0.0.1:8000'
        self.create_toke_url: str = '/auth/jwt/create/'

        self.list_teachers_file_url: str = '/api/v1/teachers/files/'
        self.detail_teachers_file_url: str = '/api/v1/teachers/files/1/'
        self.list_teachers_url: str = '/api/v1/teachers/'
        self.detail_teachers_url: str = '/api/v1/teachers/1/'

        self.list_groups_url: str = '/api/v1/groups/'
        self.detail_groups_url: str = '/api/v1/groups/1/'
        self.list_teachers_groups_url: str = '/api/v1/groups/teachers/411/'  # In future it'll be change
        self.list_subjects_groups_url: str = '/api/v1/groups/subjects/411/'  # In future it'll be change

        self.list_subjects_url: str = '/api/v1/subjects/'
        self.detail_subjects_url: str = '/api/v1/subjects/1/'
        self.list_teachers_subjects_url: str = '/api/v1/subjects/teachers/1/'

        self.test_data: dict = {
            "username": "admin",
            "password": "rombik99"
        }

    def list_teachers_subjects(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_teachers_subjects_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_list_teachers_groups(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_teachers_groups_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_list_subjects_groups(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_subjects_groups_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_list_teachers(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_teachers_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_detail_teacher(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.detail_teachers_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_list_files_teachers(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_teachers_file_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    # def test_detail_files_teacher(self):
    #    _, token = self.create_token()
    #    response = requests.get(self.get_url(self.domain, self.detail_teachers_file_url),
    #                            headers={"Authorization": f"JWT {token}"})
    #    self.checkout(response)

    def test_list_groups(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_groups_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_detail_groups(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.detail_groups_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_list_subjects(self):
        _, token = self.create_token()
        response = requests.get(self.get_url(self.domain, self.list_subjects_url),
                                headers={"Authorization": f"JWT {token}"})
        self.checkout(response)

    def test_detail_subjects(self):
        _, token = self.create_token()
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

    def create_token(self) -> list:
        response = requests.post(self.get_url(self.domain, self.create_toke_url), self.test_data)
        token = json.loads(response.content)['data']['token']
        return [response, token]
