"""
Creator fake data
"""

import pandas as pd
import numpy as np
from faker import Faker


class FakeDataGenerator:
    """
    FakeDataGenerator - class for generate fake dataset
    """
    def __init__(self, column_types: dict, column_ranges: dict, num_values: int):
        self.column_types = column_types
        self.column_ranges = column_ranges
        self.num_values = num_values
        self.fake = Faker()

    """
     Initialize the FakeDataGenerator class.

     #todo сделать установку размеров для генерации (дата диапазон, числа диапазон и так далее)
     #todo сделать генерацию через yeald обсудить

     :param column_types: Dictionary containing column names and their corresponding faker formats.
                             Example: {'name': 'name', 'age': 'random_int'}
     :param column_ranges: Number of rows to generate
     :param num_values: Format in which to return the fake data. Options: "dataframe" or "dict"

     """

    def generate_dataset(self) -> pd.DataFrame:
        """
        Generate fake dataset
        :return: pd.DataFrame
        """
        data = {}
        for column, data_type in self.column_types.items():
            if data_type == "int":
                if column in self.column_ranges:
                    start, end = self.column_ranges[column]
                    data[column] = np.random.randint(start, end + 1, self.num_values)
                else:
                    data[column] = np.random.randint(0, 100, self.num_values)
            elif data_type == "str":
                data[column] = [self.fake.word() for _ in range(self.num_values)]
            elif data_type == "float":
                if column in self.column_ranges:
                    start, end = self.column_ranges[column]
                    data[column] = np.random.uniform(start, end, self.num_values)
                else:
                    data[column] = np.random.uniform(0.0, 100.0, self.num_values)
            else:
                data[column] = [
                    getattr(self.fake, data_type)() for _ in range(self.num_values)
                ]

        return pd.DataFrame(data)
