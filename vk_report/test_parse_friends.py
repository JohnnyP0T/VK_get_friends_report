import unittest

from vk_report.parse_friends import *


class ParseFriendsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data_test =[{'id': 5954849, 'bdate': '15.5.1989', 
        'city': {'id': 144, 'title': 'Томск'}, 
        'country': {'id': 1, 'title': 'Россия'}, 
        'track_code': '1b61a86cP6Ck4MpMnX5L5NtADDJrdDKtyDpI9-Xy6mmjK4mTCHZSy6vYrxjHc0zu752k1PMFS67IUy2ZgQ', 
        'sex': 2, 
        'first_name': 'Алексей', 'last_name': 'Калентьев', 'can_access_closed': True, 
        'is_closed': False}, {'id': 34559627, 'city': {'id': 160, 'title': 'Грозный'}, 
        'country': {'id': 1, 'title': 'Россия'}, 
        'track_code': '0e9bb124ml_Hy-NPBzs_3lT8JqCOBeTKA3MTm6y_ue_sozHqSJ_3NM_50k8GOjreYyq_LRpnhMcUaHb1yMw', 
        'sex': 2, 'first_name': 'Иван', 'last_name': 'Неверов', 'can_access_closed': True, 'is_closed': True} ]

    def test_save_is_exist_json(self) -> None:
        # Arrange

        # Act
        data_actual = parse_friends(self.data_test)

        #Assert
        data_expected = [{'first_name': 'Алексей', 'last_name': 'Калентьев', 'country': 'Россия', 
        'city': 'Томск', 'birth_date': '1989-05-15T00:00:00', 'sex': 'male'}, 
        {'first_name': 'Иван', 'last_name': 'Неверов', 'country': 'Россия', 
        'city': 'Грозный', 'birth_date': 'unknown', 'sex': 'male'}]
        self.assertEqual(data_actual, data_expected)

