import sys


from src.vk_report.vk_api import Vkapi
from src.writer.csv_tsv_writer import WriterCsvTsv
from src.writer.json_writer import WriterJson
from src.console_args_parser.parser_args import parse_arg


def main():
    namespace = parse_arg(sys.argv[1:])
    print('receiving data')
    vk = Vkapi(user_id=namespace.user_id, token=namespace.token)
    data = vk.get_friends()
    data.sort(key=lambda x: x['first_name'])
    print('data received')
    if namespace.format == 'csv':
        writer = WriterCsvTsv()
        writer.write(file_name=f'{namespace.path}.csv', data=data)
    elif namespace.format == 'tsv':
        writer = WriterCsvTsv('\t')
        writer.write(file_name=f'{namespace.path}.tsv', data=data)
    elif namespace.format == 'json':
        writer = WriterJson(4)
        writer.write(file_name=f'{namespace.path}.json', data=data)
    else:
        print('unknown error')
    print('report recorded')


if __name__ == '__main__':
    main()
