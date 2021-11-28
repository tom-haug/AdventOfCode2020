import day21_common as common

def get_part01_result(file_name: str):
    foods_list = common.FoodList(file_name)
    non_allergen_ingredients = foods_list.get_non_allergen_ingredients()
    all_non_allergen_ingredient_occurance_count = foods_list.get_occurances_of_ingredients(non_allergen_ingredients)
    return all_non_allergen_ingredient_occurance_count


if __name__ == '__main__':
    file_name = 'input.txt'

    result = get_part01_result(file_name)
    print(result)
