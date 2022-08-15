import requests
import sys

from vk_report.parse_friends import *


class Vkapi:
    def __init__(self, user_id: int, token: str):
        self.token = token
        self.user_id = user_id

    def get_friends(self) -> dict:
        response = requests.get(
            f'https://api.vk.com/method/friends.get?user_id={int(self.user_id)}&'
            f'fields=bdate,country,city,sex&'
            f'access_token={self.token}&v=5.131').json()
        if 'error' in response:
            print(response.get('error').get('error_msg'))
            sys.exit()
        else:
            response = response.get('response')
        if 'items' not in response:
            print('unknown error')
        return parse_friends(response['items'])
