import pandas as pd

from database import connect_to_database


def import_data_into_dataframes(file_path: str):
    df = pd.read_csv(file_path)