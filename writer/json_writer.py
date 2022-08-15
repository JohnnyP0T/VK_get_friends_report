import json

"""Сохранение данных в json файл.

"""
class WriterJson():
    def __init__(self, indent:int=4):
        self.indent = indent

    def write(self, file_name:str, data):
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=self.indent)
