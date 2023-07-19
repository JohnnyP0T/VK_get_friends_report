import sys
import argparse
import logging

from vk_report.vk_api import VkApi
from vk_report.friends_report import FriendsReport
from writer.csv_tsv_writer import WriterCsvTsv
from writer.json_writer import WriterJson
from vk_report.exceptions import VkApiException


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='VK_get_friends_report',
        description='Improvado Back-end test task for Junior',
        epilog='2023'
    )
    parser.add_argument('-t', '--token', required=True, help='access token vk')
    parser.add_argument('-u', '--user_id', type=int, required=True, help='vk user_id')
    parser.add_argument('-f', '--format', choices=['csv', 'tsv', 'json'], default='csv', help='format file')
    parser.add_argument('-p', '--path', default='report', help='path file save no extension')

    return parser

def main():
    logging.basicConfig(level=logging.DEBUG)
    version = '5.131'
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    logging.debug('receiving data')
    vk = VkApi(token=args.token, version=version)
    report = FriendsReport(api=vk)
    try:
        data = report.get_data(user_id=args.user_id)
    except VkApiException as e:
        logging.error(str(e))
        return

    data.sort(key=lambda x: x['first_name'])
    logging.debug('data received')
    if args.format == 'csv':
        writer = WriterCsvTsv()
        writer.write(file_name=f'{args.path}.csv', data=data)
    elif args.format == 'tsv':
        writer = WriterCsvTsv('\t')
        writer.write(file_name=f'{args.path}.tsv', data=data)
    elif args.format == 'json':
        writer = WriterJson(4)
        writer.write(file_name=f'{args.path}.json', data=data)
    else:
        logging.error('unknown format')
        raise ValueError('unknown format')
    
    logging.debug(f'file is written on {args.format} format')
    logging.debug('report recorded')


if __name__ == '__main__':
    main()
