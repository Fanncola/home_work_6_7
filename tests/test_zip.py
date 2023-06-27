import zipfile
from zipfile import ZipFile
import os
from conftest import RES_PATH, TMP_PATH


def test_create_and_read_zip(file_manager):
    file_path = os.listdir(RES_PATH)
    file_name = 'new_arch.zip'

    with zipfile.ZipFile(os.path.join(TMP_PATH, file_name), mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zip:
        for file in file_path:
            file_add = os.path.join(RES_PATH, file)
            zip.write(file_add)

    with ZipFile(os.path.join(TMP_PATH, 'new_arch.zip')) as zip:
        file_names = [os.path.basename(file) for file in zip.namelist()]
        assert file_names == os.listdir(RES_PATH)

