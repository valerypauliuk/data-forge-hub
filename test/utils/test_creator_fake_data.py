import unittest

from utils.faker.creator_fake_data import FakeDataGenerator


class TestFakeDataGenerator(unittest.TestCase):
    """
    Unit test
    """
    column_types = {
        "A": "int",
        "B": "str",
        "C": "float",
        "name": "name",
        "email": "email",
        "date": "date",
    }
    column_ranges = {"A": (1, 10), "C": (0.0, 10.0)}
    num_values = 10

    def test_num_columns(self) -> None:
        """
        Test without kar_active, need check auto add kar_active
        Returns: None
        """
        dataset_generator = FakeDataGenerator(self.column_types,
                                              self.column_ranges,
                                              self.num_values)
        dataset = dataset_generator.generate_dataset()

        columns_name = len(list(dataset.columns))
        self.assertTrue(columns_name == 6)

    def test_count_rows(self) -> None:
        """
        Test without kar_active, need check auto add kar_active
        Returns: None
        """
        dataset_generator = FakeDataGenerator(self.column_types,
                                              self.column_ranges,
                                              self.num_values)
        dataset = dataset_generator.generate_dataset()

        count_rows = dataset.shape
        self.assertTrue(count_rows[0] == 10)
