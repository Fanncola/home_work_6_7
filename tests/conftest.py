import pytest
import os
import glob

TMP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))
RES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))


@pytest.fixture()
def file_manager():
    if not os.path.exists(TMP_PATH):
        os.makedirs(TMP_PATH)

    yield
    files = glob.glob(os.path.join(TMP_PATH, '*'))
    for f in files:
        os.remove(f)
