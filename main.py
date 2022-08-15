import sys
import argparse

from vk_report import vkaip
from writer.csv_tsv_writer import WriterCsvTsv

# debug




def createParser():
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
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    #if len(sys.argv) == 1:
    #    print('not enough parameters -h help')
    #if len(sys.argv) > 8:
    #    print()
    #if (sys.argv[1] == '-h' or
    #        sys.argv[1] == '-help'):
    #    print('-t --token [access token vk] \n'
    #          '-u --user_id [vk user_id] \n'
    #          '-f --format [format file] csv(default) tsv json \n'
    #          '-p --path [path file save]')
    v = vkaip.Vkapi(user_id=ID, token=TOKEN)
    r1 = v.get_friends()
    writer = WriterCsvTsv(delimiter='\n')
    writer.write(file_name='report', data=r1)


if __name__ == '__main__':
    main()
