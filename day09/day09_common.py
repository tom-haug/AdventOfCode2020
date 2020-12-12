def load_number_list_from_file(file_path) -> list[int]:
    f = open(file_path, "r")
    input_lines = f.read().splitlines()
    nums = [int(line) for line in input_lines]
    return nums


def is_sum_of_two_items_in_list(check_item: int, partial_list: list[int]):
    for num1_idx in range(len(partial_list)):
        for num2_idx in range(num1_idx + 1, len(partial_list)):
            num1 = partial_list[num1_idx]
            num2 = partial_list[num2_idx]
            if num1 + num2 == check_item:
                return True
    return False


def find_first_invalid_num(num_list, check_item_count):
    for test_num in range(check_item_count, len(num_list) - 1):
        check_item = num_list[test_num]
        partial_list = num_list[test_num - check_item_count: test_num]
        keep_going = is_sum_of_two_items_in_list(check_item,partial_list)
        if not keep_going:
            return check_item
    raise Exception("no invalid numbers in list")


def find_contiguous_sum_to_target(num_list, sum_target) -> list[int]:
    for start_idx in range(len(num_list)):
        end_idx = start_idx
        while sum(num_list[start_idx: end_idx]) < sum_target:
            end_idx += 1
        if sum(num_list[start_idx: end_idx]) == sum_target:
            return num_list[start_idx: end_idx]
    return None


def find_encryption_weakness_from_sum_target(num_list, sum_target):
    found_list = find_contiguous_sum_to_target(num_list, sum_target)

    if found_list is None:
        raise Exception("find_contiguous_sum_to_target returned None")

    list_min = min(found_list)
    list_max = max(found_list)
    encryption_weakness = list_min + list_max
    return encryption_weakness


def find_encryption_weakness_from_initial_input(num_list, check_item_count):
    first_invalid_num = find_first_invalid_num(num_list, check_item_count)
    encryption_weakness = find_encryption_weakness_from_sum_target(num_list, first_invalid_num)
    return encryption_weakness
