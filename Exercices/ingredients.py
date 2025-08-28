ingredients_required = {'flour', 'sugar', 'milk', 'yogurt', 'butter', 'eggs'}

user_input = input('Which ingredients do you have?: ')
user_ingredients = set(user_input.split(', '))

#ingredients_missing = ingredients_required.difference(user_ingredients)
ingredients_missing = ingredients_required - user_ingredients
extras_ingredients = user_ingredients.difference(ingredients_required)
extras_ingredients = user_ingredients - ingredients_required

if ingredients_missing:
    print(f'Missing ingredients: {', '.join(ingredients_missing)}')
    # print('Missing ingredients:', ', '.join(ingredients_missing))
else:
    print("No missing ingredients")

if extras_ingredients:
    print(f'Extras ingredients: {', '.join(extras_ingredients)}')
    # print('Extras ingredients:', ', '.join(extras_ingredients))
else:
    print("No extras ingredients")