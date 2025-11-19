import unittest
from city_functions import city_country


class TestCityFunctions(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Los Angeles", "USA")
        self.assertEqual(result, "Los Angeles, USA")


if __name__ == '__main__':
    unittest.main()