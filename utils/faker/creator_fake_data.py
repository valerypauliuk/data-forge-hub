"""
Creator fake data
"""

import pandas as pd
from faker import Faker


class FakeDataGenerator:
    def __init__(self,
                 columns_formats: dict,
                 num_rows: int,
                 data_format="dataframe"
                 ):
        """
        Initialize the FakeDataGenerator class.

        #todo сделать установку размеров для генерации (дата диапазон, числа диапазон и так далее)
        #todo сделать генерацию через yeald обсудить

        :param columns_formats: Dictionary containing column names and their corresponding faker formats.
                                Example: {'name': 'name', 'age': 'random_int'}
        :param num_rows: Number of rows to generate
        :param data_format: Format in which to return the fake data. Options: "dataframe" or "dict"

        """
        self.columns_formats = columns_formats
        self.data_format = data_format
        self.num_rows = num_rows or 100
        self.fake = Faker()

    def generate_fake_data(self):
        """
        Generate fake data based on the provided column formats.

        :return: Fake data in the specified format.
        """
        data = {}
        for column, faker_format in self.columns_formats.items():
            data[column] = [getattr(self.fake, faker_format)() for _ in range(self.num_rows)]

        if self.data_format == "dataframe":
            return pd.DataFrame(data)
        elif self.data_format == "dict":
            return data
        else:
            raise ValueError("Invalid data format. Choose either 'dataframe' or 'dict'.")
