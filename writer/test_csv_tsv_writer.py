import unittest
import os

from writer.csv_tsv_writer import WriterCsvTsv


class CsvTsvTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name_test = f'{os.getcwd()}/tests_data/report_test.csv'
        self.file_name_test_sample = f'{os.getcwd()}/tests_sample/report_test_sample.csv'

        self.data_test = [
            {
                'first_name': 'Alexander',
                'last_name': 'Potlog',
                'country': 'Russia',
                'city': 'Tomsk',
                'birth_date': '1900-01-31T00:00:00',
                'sex': 'male'
            },
            {
                'first_name': 'Ivan',
                'last_name': 'Ivanovich',
                'country': 'America',
                'city': 'New York',
                'birth_date': '1900-09-17T00:00:00',
                'sex': 'male'
            }
        ]
        if not os.path.exists('tests_data'):
            os.mkdir('tests_data')
        if os.path.isfile(self.file_name_test):
            os.remove(self.file_name_test)

    def test_save_is_exist_json(self) -> None:
        # Arrange
        writer_test = WriterCsvTsv()

        # Act
        writer_test.write(file_name=self.file_name_test, data=self.data_test)

        # Assert
        self.assertTrue(os.path.isfile(self.file_name_test))

    def test_save_correct_data(self) -> None:
        # Arrange
        writer_test = WriterCsvTsv()

        # Act
        writer_test.write(file_name=self.file_name_test, data=self.data_test)

        # Assert
        with open(self.file_name_test, 'r') as file:
            data_actual = file.read()
        with open(self.file_name_test_sample, 'r') as file:
            data_expected = file.read()
        self.assertEqual(data_actual, data_expected)
