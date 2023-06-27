import os.path
from conftest import RES_PATH

from pypdf import PdfReader


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_open_pdf_file():
    file_name = 'docs-pytest-org-en-latest.pdf'
    reader = PdfReader(os.path.join(RES_PATH, file_name))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    assert number_of_pages == 412
    assert 'pytest Documentation\nRelease 0.1' in text
