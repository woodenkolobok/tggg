class Meal:
    def __init__(self, price: int, 
                 ingredients: list[str], 
                 name: str, 
                 description: str):
        self.price = price
        self.ingredients = ingredients
        self.name = name
        self.desctiption = description

    def __str__(self):
        result = f'Название: {self.name}\n'
        result += 'Ингридиенты:\n'
        for ingredient in self.ingredients:
            result += f'\t-{ingredient}\n'
        result += f'Цена: {self.price} рублей\n'
        result += f'Описание: {self.desctiption}\n\n'
        return result


class MealContainer:
    def __init__(self, meals: list[Meal]):
        self.meals = meals

    def write_to_file(self):
        f = open('meals.txt', 'w+', encoding='utf-8')
        f.write('Блюда:\n')
        for meal in self.meals:
            f.write(str(meal))
        f.close()

kurica = Meal(price=4000,
              ingredients=['просроченная курица',
                           'штукатурка'],
                name = 'Просроченная курица',
                description='Курица с ближайшей помойки')
potato = Meal(price=200,
              ingredients=['картошка?'],
              name='Картошка!',
              description='Картошка.')
soup = Meal(price=1_000_000,
            ingredients=['волосы полковника Сандерса'
                         'вода',
                         'соль'
                         'перец'],
            name='Суп из волос полковника Сандерса',
            description='Суп.')

meal_container = MealContainer(meals=[kurica, potato, soup])
meal_container.write_to_file()