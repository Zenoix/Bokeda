import sqlite3
from pathlib import PurePath, Path


def connect_to_database():
    location = PurePath(Path(__file__).parent.resolve(), "categories.db")
    con = sqlite3.connect(location)
    return con
