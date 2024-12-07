from abc import ABC, abstractmethod
from typing import List, Dict, Any
import csv
import json
import xml.etree.ElementTree as ET

# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

# Step 2: Implement the file parsers
# TODO: Implement CSVParser, JSONParser, and XMLParser classes
class CSVParser(FileParser):

    def parse_file(self, file_path: str):
        Dict_list = []
        List_values = []
        keys = []
        values = []

        rows = 0

        def return_dict(key, values_csv):
            Dict = {}
            Dict[key] = values_csv
            return Dict

        def return_keys(file_path):
            with open(file_path, '+r') as file:
                reader = csv.reader(file)
                keys = next(reader)
            return keys

        keys = return_keys(file_path)
        with open(file_path, '+r') as file:

            for line in file:
                rows += 1
                if rows > 1:
                    values = line.split(",")
                    for i in range(len(values)):
                        dictionary = return_dict(keys[i], values[i])
                        Dict_list.append(dictionary)

        return Dict_list


class JSONParser(FileParser):
    def parse_file(self, file_path: str):
        with open(file_path, 'r') as j:
            contents = json.loads(j.read())

        return contents

class XMLParser(FileParser):
    def parse_file(self, file_paht:str):
        tree = ET.parse(file_paht)
        root = tree.getroot()
        Dict_list = []
        for child in root:
            #print(child.tag, child.attrib)
            Dict_list.append(child.attrib)
        return Dict_list


# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self.file_parser=file_parser


    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser
        return self.file_parser.parse_file(file_path)

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(CSVParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file("sample.csv")
    print(data)

    reader_json = FileReader(JSONParser())
    data_json = reader_json.read_file("sample.json")
    print(data_json)

    reader_xml = FileReader(XMLParser())
    data_xml = reader_xml.read_file("sample.xml")
    print(data_xml)