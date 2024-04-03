import os
import zipfile
import pytest

files = ["Python Notes.pdf", "example.xlsx", "example3.csv"]


@pytest.fixture(scope="session", autouse=True)
def archive_creation():
    files_list = ["Python Notes.pdf", "example.xlsx", "example3.csv"]
    if not os.path.exists("resource"):
        os.mkdir("resource")
        with zipfile.ZipFile("resource/archive.zip", "a") as arch:
            os.chdir("temp")
            for file in files_list:
                arch.write(file)
    os.chdir("resource")

    yield

    if os.path.exists("resource/archive.zip"):
        os.remove("resource/archive.zip")
    if os.path.exists("resource"):
        os.rmdir("resource")
