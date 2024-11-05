##controller du telechargement de csv
import csv
import uuid

from app.config.config import config
from app.classs.interfaces.Icontroller import Icontroller
from app.classs.entities.Calcul import Calcul

class dowloadCTRL(Icontroller):
    headers = []
    def post(self):
        pass
    def get(self):
        path = config.get_attr("DOWLOAD_PATH")
        file_name = str(uuid.uuid4()) + '.csv'
        csv_file_path = path + file_name
        self.create_empty_csv(csv_file_path)
        self.write_header(csv_file_path)
        self.write_rows(csv_file_path)

        return [path, file_name]

    def create_empty_csv(self, file_path):
        with open(file_path, mode='w', newline='') as csv_file:
            pass
    def write_rows(self, file_path):
        select = Calcul.select()
        result = []
        for calcul in select:
            arr_tmp = []
            for header in self.headers:
                arr_tmp.append(getattr(calcul,header))
            result.append(arr_tmp)
        with open(file_path, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(result)

    def write_header(self, file_path):
        columns = Calcul._meta.sorted_fields
        self.headers = []
        for column in columns:
            self.headers.append(column.name)
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.headers)