import sys
import argparse
import time

from vk_report import vkaip
from writer.csv_tsv_writer import WriterCsvTsv
from writer.json_writer import WriterJson


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='VK_get_friends_report',
        description='Improvado Back-end test task for Junior',
        epilog='2022'
    )
    parser.add_argument('-t', '--token', required=True, help='access token vk')
    parser.add_argument('-u', '--user_id', type=int, required=True, help='vk user_id')
    parser.add_argument('-f', '--format', choices=['csv', 'tsv', 'json'], default='csv', help='format file')
    parser.add_argument('-p', '--path', default='reports', help='path file save')

    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    print('receiving data')
    vk = vkaip.Vkapi(user_id=namespace.user_id, token=namespace.token)
    data = vk.get_friends()
    data.sort(key=lambda x: x['first_name'])
    print('data received')
    if namespace.format == 'csv':
        writer = WriterCsvTsv()
        writer.write(file_name='report.csv', data=data)
    elif namespace.format == 'tsv':
        writer = WriterCsvTsv('\t')
        writer.write(file_name='report.tsv', data=data)
    elif namespace.format == 'json':
        writer = WriterJson(4)
        writer.write(file_name='report.json', data=data)
    else:
        print('unknown error')
    print('report recorded')


if __name__ == '__main__':
    main()
