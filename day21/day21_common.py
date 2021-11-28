import os
import sys

class Ingredient:
    def __init__(self, name: str, allergen: str):
        self.name = name
        self.allergen = allergen


class Food:
    def __init__(self, input_text: str):
        (ingredients_text, allergens_text) = self.split_ingredients_allergens(input_text)
        ingredients_str_list = ingredients_text.split(" ")
        allergens_str_list = [] if allergens_text == '' else allergens_text.split(", ")

        self.ingredients = ingredients_str_list #[Ingredient(ingredient_name, allergens_str_list) for ingredient_name in ingredients_str_list]
        self.allergens: list[str] = allergens_str_list

    def split_ingredients_allergens(self, input_line: str) -> (str, str):
        sections = [section.strip(" )") for section in input_line.split("(")]
        return (sections[0], "" if len(sections) == 1 else sections[1].replace("contains ", ""))


    def __str__(self):
        return f"Food - Ingredients({len(self.ingredients)})={', '.join(self.ingredients)}, Allergens({len(self.allergens)})={', '.join(self.allergens)}"


class FoodList():

    def __init__(self, file_name: str):
        self._foods = self.__load_input_from_file(file_name)


    def get_non_allergen_ingredients(self) -> list[str]:
        ingredients_with_allergens = self.get_allergen_ingredients()
        all_ingredients = self.__get_all_ingredients_in_foods()
        ingredients_without_allergen = [ingredient for ingredient in all_ingredients if ingredient not in map(lambda ingredient: ingredient.name, ingredients_with_allergens)]

        return ingredients_without_allergen


    def get_allergen_ingredients(self) -> list[Ingredient]:
        all_allergens = self.__get_all_allergens_in_foods()

        ingredients_with_known_allergen: list[Ingredient] = []

        keep_processing = True

        while keep_processing:
            keep_processing = False
            for allergen in all_allergens:
                foods_with_current_allergen = list(filter(lambda food: allergen in food.allergens, self._foods))
                ingredients_in_common = self.__get_ingredients_in_common(foods_with_current_allergen)
                ingredient_names_with_known_allergen = [ingredient.name for ingredient in ingredients_with_known_allergen]
                ingredients_in_common = list(filter(lambda ingredient: ingredient not in ingredient_names_with_known_allergen, ingredients_in_common))
                if len(ingredients_in_common) == 1:
                    keep_processing = True
                    ingredients_with_known_allergen.append(Ingredient(ingredients_in_common[0], allergen))

        return ingredients_with_known_allergen


    def get_occurances_of_ingredients(self, ingredients: list[str]):
        count = 0
        for ingredient in ingredients:
            count += self.__get_ingredient_occurance_count(ingredient)
        return count


    def __load_input_from_file(self, file_name: str) -> list[Food]:
        file_path = os.path.join(sys.path[0], file_name)
        f = open(file_path, "r")
        file_contents = f.read()
        f.close()

        foods = [Food(input_line) for input_line in file_contents.splitlines()]
        return foods


    def __get_all_allergens_in_foods(self) -> list[str]:
        all_allergens: Set[str] = set()
        for food in self._foods:
            for allergen in food.allergens:
                all_allergens.add(allergen)
        return list(all_allergens)


    def __get_all_ingredients_in_foods(self) -> list[str]:
        all_ingredients: Set[str] = set()
        for food in self._foods:
            for ingredient in food.ingredients:
                all_ingredients.add(ingredient)
        return list(all_ingredients)


    def __get_ingredients_in_common(self, foods: list[Food]) -> list[str]:
        ingredients_in_common = list(foods[0].ingredients)
        for food in foods:
            ingredients_in_common = list(filter(lambda cur_food_ingredient: cur_food_ingredient in ingredients_in_common, food.ingredients))
        return ingredients_in_common


    def __get_ingredient_occurance_count(self, ingredient: str):
        foods_with_ingredient = [food for food in self._foods if ingredient in food.ingredients]
        return len(foods_with_ingredient)
