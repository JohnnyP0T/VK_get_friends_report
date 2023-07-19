import argparse
import pytest
from parser_args import parse_arg


def test_parse_arg_valid_arguments():
    # Подготовка тестовых данных
    args = ['VK_get_friends_report', '-t', 'your_token', '-u', '123', '-f', 'csv', '-p', 'report']

    # Выполнение функции
    result = parse_arg(args)

    # Проверка результатов
    assert result.token == 'your_token'
    assert result.user_id == 123
    assert result.format == 'csv'
    assert result.path == 'report'


def test_parse_arg_missing_required_arguments():
    # Подготовка тестовых данных
    args = ['VK_get_friends_report', '-u', '123']

    # Выполнение функции и проверка на возникновение исключения
    with pytest.raises(SystemExit):
        parse_arg(args)


def test_parse_arg_invalid_arguments():
    # Подготовка тестовых данных
    args = ['VK_get_friends_report', '-t', 'your_token', '-u', '123', '-f', 'invalid_format', '-p', 'report']

    # Выполнение функции и проверка на возникновение исключения
    with pytest.raises(SystemExit):
        parse_arg(args)


def test_parse_arg_token():
    parsed = parse_arg(['VK_get_friends_report', '-t', 'long', '-u', '123'])
    assert parsed.token == 'long'


def test_parse_arg_user_id():
    parsed = parse_arg(['VK_get_friends_report', '-t', 'long', '-u', '123'])
    assert parsed.user_id == 123


def test_parse_arg_format():
    parsed = parse_arg(['VK_get_friends_report', '-t', 'long', '-u', '123', '-f', 'json'])
    assert parsed.format == 'json'


def test_parse_arg_no_format():
    parsed = parse_arg(['VK_get_friends_report', '-t', 'long', '-u', '123'])
    assert parsed.format == 'csv'


def test_parse_arg_uncorrect_user_id():
    with pytest.raises(SystemExit):
        parse_arg(['VK_get_friends_report', '-t', 'long', '-u', 'bebra'])


def test_parse_arg_uncorrect_format():
    with pytest.raises(SystemExit):
        parse_arg(['VK_get_friends_report', '-t', 'long', '-u', '123', '-f', 'yaml'])
