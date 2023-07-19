import pytest
from parse_friends import *


@pytest.fixture
def sample_data():
    return [{'id': 5954849, 'bdate': '15.5.1989', 'city': {'id': 144, 'title': 'Томск'},
             'country': {'id': 1, 'title': 'Россия'}, 'track_code': '1b61a86cP6Ck4MpMnX5L5NtADDJrdDKtyDpI9-Xy6mmjK4mTCHZSy6vYrxjHc0zu752k1PMFS67IUy2ZgQ', 'sex': 2,
             'first_name': 'Алексей', 'last_name': 'Калентьев', 'can_access_closed': True, 'is_closed': False},
            {'id': 34559627, 'city': {'id': 160, 'title': 'Грозный'}, 'country': {'id': 1, 'title': 'Россия'},
             'track_code': '0e9bb124ml_Hy-NPBzs_3lT8JqCOBeTKA3MTm6y_ue_sozHqSJ_3NM_50k8GOjreYyq_LRpnhMcUaHb1yMw', 'sex': 2,
             'first_name': 'Иван', 'last_name': 'Неверов', 'can_access_closed': True, 'is_closed': True}]


def test_parse_friends_country():
    assert parse_friends_country({'id': 1, 'title': 'Россия'}) == 'Россия'
    assert parse_friends_country(None) == 'unknown'


def test_parse_friends_city():
    assert parse_friends_city({'id': 144, 'title': 'Томск'}) == 'Томск'
    assert parse_friends_city(None) == 'unknown'


def test_parse_friends_birth_date():
    assert parse_friends_birth_date('15.5.1989') == '1989-05-15'
    assert parse_friends_birth_date('15.5') == '1900-05-15'
    assert parse_friends_birth_date(None) == 'unknown'


def test_parse_friends_sex():
    assert parse_friends_sex(2) == 'male'
    assert parse_friends_sex(1) == 'female'
    assert parse_friends_sex(None) == 'unknown'


def test_parse_friends(sample_data):
    data_actual = parse_friends(sample_data)
    data_expected = [{'first_name': 'Алексей', 'last_name': 'Калентьев', 'country': 'Россия', 'city': 'Томск',
                      'birth_date': '1989-05-15', 'sex': 'male'},
                     {'first_name': 'Иван', 'last_name': 'Неверов', 'country': 'Россия', 'city': 'Грозный',
                      'birth_date': 'unknown', 'sex': 'male'}]
    assert data_actual == data_expected


def test_parse_friends_additional_cases():
    # Test case with missing fields
    data = [{'first_name': 'John', 'last_name': 'Doe'}]
    data_actual = parse_friends(data)
    data_expected = [{'first_name': 'John', 'last_name': 'Doe', 'country': 'unknown', 'city': 'unknown',
                      'birth_date': 'unknown', 'sex': 'unknown'}]
    assert data_actual == data_expected

    # Test case with different sex value
    data = [{'first_name': 'Jane', 'last_name': 'Doe', 'sex': 3}]
    data_actual = parse_friends(data)
    data_expected = [{'first_name': 'Jane', 'last_name': 'Doe', 'country': 'unknown', 'city': 'unknown',
                      'birth_date': 'unknown', 'sex': 'unknown'}]
    assert data_actual == data_expected
