import os
import zipfile

import pytest

ROOT_PATH = os.getcwd()
TMP = os.path.join(ROOT_PATH, "temp")
RES = os.path.join(ROOT_PATH, "resource")
ARCH = os.path.join(RES, "archive.zip")


@pytest.fixture(scope="session", autouse=True)
def archive_creation():
    files_list = ["Python Notes.pdf", "example.xlsx", "example3.csv"]
    if not os.path.exists(RES):
        os.mkdir(RES)
    with zipfile.ZipFile(f"{RES}/archive.zip", "a") as arch:
        os.chdir(TMP)
        for file in files_list:
            arch.write(file)

    yield

    if os.path.exists(ARCH):
        os.remove(ARCH)
    if os.path.exists(RES):
        os.rmdir(RES)
