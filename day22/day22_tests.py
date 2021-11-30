import unittest
import day22_part01 as part01
import day22_part02 as part02

class TestDay22(unittest.TestCase):
    def test_part01(self):
        file_name = "input_sample01.txt"
        (winning_player_number, winning_score) = part01.get_part01_result(file_name)
        self.assertEqual(winning_score, 306)

    def test_part02(self):
        file_name = "input_sample01.txt"
        (winning_player_number, winning_score) = part02.get_part02_result(file_name)
        self.assertEqual(winning_score, 291)


if __name__ == '__main__':
    unittest.main()
