import csv


class WriterCsvTsv:
    def __init__(self, delimiter: str = ','):
        self._delimiter = delimiter

    def write(self, file_name: str, data:list) -> None:
        with open(file_name, 'w', encoding='utf-8') as file:
            fieldnames = ['first_name', 'last_name', 'country', 'city', 'birth_date', 'sex']

            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=self._delimiter)
            writer.writeheader()
            for person in data:
                writer.writerow({'first_name': person['first_name'], 'last_name': person['last_name'],
                                 'country': person['country'], 'city': person['city'],
                                 'birth_date': person['birth_date'], 'sex': person['sex']})

