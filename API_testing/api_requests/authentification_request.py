import random
from random import randint

import requests


def get_token():
    base_url = "https://simple-books-api.glitch.me"
    random_int = randint(1, 9999)
    client_names = [
                        'Emma',
                        'Liam',
                        'Olivia',
                        'Noah',
                        'Ava',
                    ]
    body = {
                "clientName": f"{random.choice(client_names)}",
                "clientEmail": f"account_{random_int}@example.com"
            }
    response = requests.post(f"{base_url}/api-clients/", json=body)
    return response.json()["accessToken"]