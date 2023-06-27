import os.path
import requests
from conftest import TMP_PATH


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
def test_get_file_with_requests(file_manager):
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    file_name = 'selenium_logo.png'

    file_path = os.path.abspath(os.path.join(TMP_PATH, file_name))

    assert os.path.exists(TMP_PATH)
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    assert os.path.exists(file_path)

    size = os.path.getsize(file_path)
    assert size == 30803
