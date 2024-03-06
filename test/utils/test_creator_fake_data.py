import unittest

from utils.faker.creator_fake_data import FakeDataGenerator


class TestFakeDataGenerator(unittest.TestCase):
    """
    Unit test
    """
    columns_formats = {'name': 'name', 'age': 'random_int', 'email': 'email'}

    def test_num_columns(self) -> None:
        """
        Test without kar_active, need check auto add kar_active
        Returns: None
        """
        generator = FakeDataGenerator(self.columns_formats, data_format="dataframe", num_rows=10)
        fake_data_df = generator.generate_fake_data()

        columns_name = len(list(fake_data_df.columns))
        self.assertTrue(columns_name == 3)

    def test_count_rows(self) -> None:
        """
        Test without kar_active, need check auto add kar_active
        Returns: None
        """
        generator = FakeDataGenerator(self.columns_formats, data_format="dataframe", num_rows=10)
        fake_data_df = generator.generate_fake_data()

        count_rows = fake_data_df.shape
        self.assertTrue(count_rows[0] == 10)

    def test_dict_generator(self):

        generator = FakeDataGenerator(self.columns_formats, data_format="dict", num_rows=10)
        fake_data_dict = generator.generate_fake_data()
        print(fake_data_dict)
        self.assertTrue(type(fake_data_dict) is dict)