import os
import zipfile
import pytest

files = ["Python Notes.pdf", "example.xlsx", "example3.csv"]


@pytest.fixture(scope="module", autouse=True)
def archive_creation():
    files_list = ["Python Notes.pdf", "example.xlsx", "example3.csv"]
    if not os.path.exists("resource"):
        os.mkdir("resource")
    if not os.path.exists("resource/archive.zip"):
        with zipfile.ZipFile("resource/archive.zip", "a") as arch:
            os.chdir("temp")
            for file in files_list:
                arch.write(file)

    yield

    os.remove("resource/archive.zip")
    os.rmdir("resource")
