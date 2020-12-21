from day18_common import load_equations_from_file

if __name__ == '__main__':
    file_name = 'input.txt'
    operator_precedence = [['*', '+']]
    equations = load_equations_from_file(file_name, operator_precedence)
    result_sum = 0

    for idx, equation in enumerate(equations):
        result = equations[idx].evaluate()
        result_sum += result
        print(f'Equation {idx} result:', result)

    print('result sum:', result_sum)