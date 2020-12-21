from day17_common import run_simulation


if __name__ == "__main__":
    file_name = 'input.txt'
    num_dimensions = 4
    num_cycles = 6

    print('this will take a little time...')
    number_active_cubes = run_simulation(file_name, num_dimensions, num_cycles)
    print('number_active_cubes', number_active_cubes)
