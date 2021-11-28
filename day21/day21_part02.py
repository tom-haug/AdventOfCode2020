import day21_common as common

def get_part02_result(file_name: str):
    foods_list = common.FoodList(file_name)
    allergen_ingredients = foods_list.get_allergen_ingredients()

    sorted_ingredients = sorted(allergen_ingredients,key = lambda item: item.allergen)
    sorted_ingredient_names = [ingredient.name for ingredient in sorted_ingredients]

    result = ",".join(sorted_ingredient_names)
    return result


if __name__ == '__main__':
    file_name = 'input.txt'

    result = get_part02_result(file_name)
    print(result)
