import unittest

from day16_common import load_property_definitions_and_tickets_from_file, get_invalid_property_count_on_tickets
from day16_part02 import get_complete_property_definitions_and_your_ticket


class TestDay16(unittest.TestCase):
    def test_part01(self):
        # Arrange
        file_name = 'input_sample01.txt'

        # Act
        property_definitions, your_ticket, nearby_tickets = load_property_definitions_and_tickets_from_file(file_name)
        invalid_value_sum = get_invalid_property_count_on_tickets(property_definitions, nearby_tickets)

        # Assert
        self.assertEqual(invalid_value_sum, 71)

    def test_part02(self):
        # Arrange
        file_name = 'input_sample02.txt'

        # Act
        property_definitions, your_ticket = get_complete_property_definitions_and_your_ticket(file_name)

        # Assert
        self.assertEqual(len(property_definitions), 3)
        self.assertEqual(property_definitions[0].description, 'class')
        self.assertEqual(property_definitions[0].position_on_ticket, 1)
        self.assertEqual(property_definitions[1].description, 'row')
        self.assertEqual(property_definitions[1].position_on_ticket, 0)
        self.assertEqual(property_definitions[2].description, 'seat')
        self.assertEqual(property_definitions[2].position_on_ticket, 2)


if __name__ == '__main__':
    unittest.main()
