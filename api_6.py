# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RQHbfOREsnx4vgoN0_N7m1Cmbomd2Gqc
"""

import unittest
import requests

class TestSearchProductAPI(unittest.TestCase):

    def test_missing_search_product_param(self):

        api_url = "https://automationexercise.com/api/searchProduct"


        response = requests.post(api_url)


        self.assertEqual(response.status_code, 400, f"Beklenen 400 Bad Request, ancak {response.status_code} alındı")


        beklenen_mesaj = "Bad request, search_product parameter is missing in POST request."
        self.assertEqual(response.text, beklenen_mesaj, f"Beklenen mesaj: '{beklenen_mesaj}', ancak '{response.text}' alındı")

if __name__ == '__main__':
    unittest.main()