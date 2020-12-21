import unittest
from day18_common import load_equations_from_file


class TestDay18(unittest.TestCase):
    def _run_test(self, file_name: str, operator_precedence, expected_result_sum: int):
        with self.subTest([file_name, operator_precedence, expected_result_sum]):
            equations = load_equations_from_file(file_name, operator_precedence)
            result_sum = 0

            for idx, equation in enumerate(equations):
                result = equations[idx].evaluate()
                result_sum += result

            self.assertEqual(result_sum, expected_result_sum)

    def test_part01(self):
        operator_precedence = [['*', '+']]
        self._run_test(file_name='input_sample01.txt', operator_precedence=operator_precedence, expected_result_sum=71)
        self._run_test(file_name='input_sample02.txt', operator_precedence=operator_precedence, expected_result_sum=51)
        self._run_test(file_name='input_sample03.txt', operator_precedence=operator_precedence, expected_result_sum=26 + 437 + 12240 + 13632)

    def test_part02(self):
        operator_precedence = [['*'], ['+']]
        self._run_test(file_name='input_sample01.txt', operator_precedence=operator_precedence, expected_result_sum=231)
        self._run_test(file_name='input_sample02.txt', operator_precedence=operator_precedence, expected_result_sum=51)
        self._run_test(file_name='input_sample03.txt', operator_precedence=operator_precedence, expected_result_sum=46 + 1445 + 669060 + 23340)


if __name__ == '__main__':
    unittest.main()
