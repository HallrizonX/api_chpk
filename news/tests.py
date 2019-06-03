import json
import requests
from rest_framework.test import APITestCase
from rest_framework import status as st


class NewsDataTest(APITestCase):

    def setUp(self) -> None:
        self.domain: str = 'http://127.0.0.1:8000'

        self.detail_news_url: str = '/api/v1/news/1/'
        self.list_news_url: str = '/api/v1/news/'

    def test_list_news(self):
        _, token = self.create_token()

        response = requests.get(self.get_url(self.domain, self.list_news_url),
                                headers={"Authorization": f"JWT {token}"})

        # Check out status and basic word in JSON
        self.assertEqual(st.HTTP_200_OK, response.status_code)
        self.assertTrue('data' in str(json.loads(response.content)))
        self.assertTrue('result' in str(json.loads(response.content)))

        # Iteration all items in Response
        for item in json.loads(response.content)['data']['result']:
            # Check out if values aren't None
            self.assertIsNotNone(
                (item['id'], item['title'], item['short_description'], item['preview_image'], item['pub_date'])
            )
            # Check out if keys is in dict
            self.assertIn('id', item)
            self.assertIn('title', item)
            self.assertIn('short_description', item)
            self.assertIn('preview_image', item)
            self.assertIn('pub_date', item)

            # Check out if keys isn't in dict, because that keys in detail news
            self.assertNotIn('description', item)
            self.assertNotIn('images', item)

            self.assertIn('media', item['preview_image'])

    def test_detail_news(self):
        _, token = self.create_token()

        response = requests.get(self.get_url(self.domain, self.detail_news_url),
                                headers={"Authorization": f"JWT {token}"})

        # Check out status and basic word in JSON
        self.assertEqual(st.HTTP_200_OK, response.status_code)
        self.assertTrue('data' in str(json.loads(response.content)))
        self.assertTrue('result' in str(json.loads(response.content)))

        # Get current item
        item = json.loads(response.content)['data']['result']

        # Check out if values aren't None
        self.assertIsNotNone(
            (item['id'], item['title'], item['short_description'], item['preview_image'], item['pub_date'],
             item['description'], item['images'])
        )

        self.assertIn('media', item['preview_image'])

        if item['images']:
            for img in item['images']:
                self.assertIn('media', img['image'])

    def get_url(self, domain, url) -> str:
        if domain.endswith('/'):
            domain = domain[:-1]
        return f"{domain}{url}"

    def create_token(self) -> list:
        response = requests.post(self.get_url(self.domain, '/auth/jwt/create/'), {
            "username": "admin",
            "password": "rombik99"
        })
        token = json.loads(response.content)['data']['token']
        return [response, token]
