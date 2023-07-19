import pytest
from friends_report import FriendsReport
from unittest.mock import Mock

@pytest.fixture
def friends_report():
    api_mock = Mock()
    api_mock.get_friends_info.return_value = {
        'items': [
            {
                'first_name': 'Павел',
                'last_name': 'Дуров',
                'country': {'id': 1, 'title': 'Россия'},
                'city': {'id': 2, 'title': 'Санкт-Петербург'},
                'bdate': '10.10.1984',
                'sex': 2,
            }
        ]
    }
    return FriendsReport(api=api_mock)


def test_get_city(friends_report):
    result = friends_report.get_city({}, {'city': {'id': 2, 'title': 'Санкт-Петербург'}})
    assert result == {'city': 'Санкт-Петербург'}


def test_get_city_no_city(friends_report):
    result = friends_report.get_city({}, {})
    assert result == {'city': 'Unknown'}


def test_get_country(friends_report):
    result = friends_report.get_country({}, {'country': {'id': 1, 'title': 'Россия'}})
    assert result == {'country': 'Россия'}


def test_get_country_no_country(friends_report):
    result = friends_report.get_country({}, {})
    assert result == {'country': 'Unknown'}


def test_get_sex(friends_report):
    result = friends_report.get_sex({}, {'sex': 2})
    assert result == {'sex': 'Муж.'}


def test_get_birth_date(friends_report):
    result = friends_report.get_birth_date({}, {'bdate': '10.10.1984'})
    assert result == {'birth_date': '1984.10.10'}


def test_get_birth_date_no_year(friends_report):
    result = friends_report.get_birth_date({}, {'bdate': '17.10'})
    assert result == {'birth_date': '10.17'}


def test_get_birth_date_no_date(friends_report):
    result = friends_report.get_birth_date({}, {})
    assert result == {'birth_date': 'Unknown'}