# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rKdJYT5RHDn73dK1stw_NY3TfbQVgB7X
"""

import unittest
import requests

class TestGetUserDetailByEmailAPI(unittest.TestCase):

    def test_get_user_detail_by_email(self):

        api_url = "https://automationexercise.com/api/getUserDetailByEmail"


        email = "mirac@example.com"


        response = requests.get(api_url, params={"email": email})


        self.assertEqual(response.status_code, 200, f"Beklenen 200 OK, ancak {response.status_code} alındı")


        self.assertEqual(response.headers["Content-Type"], "application/json", "Cevap JSON formatında değil")


        json_data = response.json()
        self.assertIn("user_detail", json_data, "JSON içinde 'user_detail' anahtarı bulunamadı")



if __name__ == '__main__':
    unittest.main()