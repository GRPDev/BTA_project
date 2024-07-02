import json

class FileManager:
    def load_data(self, filename):
        with open(filename, "r") as file:
            loaddata = file.read()
            return loaddata

    def save_data(self, filename, data):
        with open(filename, "w") as file:
            file.write(data)
        
    def read_json(self, json_file_path):
        with open(json_file_path, "r") as file:
            readjson = json.load(file)
            return readjson
        
    def write_json(self, list_of_dicts, json_file_path):
        with open(json_file_path, "w") as file:
            json.dump(list_of_dicts, file)
       
    def add_to_json(self, data, json_file_path):
        data_in_json = self.read_json(json_file_path)
        data_in_json.append(data)
        self.write_json(data_in_json, json_file_path) 