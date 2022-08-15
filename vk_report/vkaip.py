import requests
import sys

from vk_report.parse_friends import *


class Vkapi:
    def __init__(self,  user_id, token):
        self.token = token
        self.user_id = user_id

    def get_friends(self):
        response = requests.get(
            f'https://api.vk.com/method/friends.get?user_id={int(self.user_id)}&'
            f'fields=bdate,country,city,sex&'
            f'access_token={self.token}&v=5.131').json()#['response']
        if 'error' in response:
            print(response.get('error').get('error_msg'))
            sys.exit()
        else:
            response = response['response']
        return parse_friends(response['items'])
