import argparse
from argparse import Namespace


def parse_arg(args: list[str]) -> Namespace:
    parser = argparse.ArgumentParser(
        prog='VK_get_friends_report',
        description='Improvado Back-end test task for Junior',
        epilog='2023'
    )
    parser.add_argument('-t', '--token', required=True, help='access token vk')
    parser.add_argument('-u', '--user_id', type=int, required=True, help='vk user_id')
    parser.add_argument('-f', '--format', choices=['csv', 'tsv', 'json'], default='csv', help='format file')
    parser.add_argument('-p', '--path', default='report', help='path file save no extension')

    return parser.parse_args(args[1:])
