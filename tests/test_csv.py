import csv
import os.path

from conftest import RES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_open_csv_file():
    test_users_1 = ['Anna', 'Pavel', 'Peter']
    test_users_2 = ['Alex', 'Serj', 'Yana']
    file_name = 'username.csv'

    with open(os.path.join(RES_PATH, file_name), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(test_users_1)
        csvwriter.writerow(test_users_2)

    assert os.path.exists(RES_PATH)

    rows = []
    with open(os.path.join(RES_PATH, file_name)) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 0:
                rows.append(row)

    assert test_users_1 in rows
    assert test_users_2 in rows
