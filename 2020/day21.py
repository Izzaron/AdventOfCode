import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'day' + str(21) + 'input.txt' )
f = open(filename)

foods = []

for line in f:
    ingredients , allergens = line.strip().replace(')','').split(' (contains ')

    ingredients = [ingredient.strip() for ingredient in ingredients.split(' ')]
    allergens = [allergen.strip() for allergen in allergens.split(', ')]

    foods.append( (ingredients,allergens) )

allergenDict = dict()

for ingredients,allergens in foods:
    for allergen in allergens:
        if allergen in allergenDict:
            allergenDict[allergen] = allergenDict[allergen].intersection(set(ingredients))
        else:
            allergenDict[allergen] = set(ingredients)

def printAllergens():
    for allergen,ingredients in allergenDict.items():
        print('Allergen: ',allergen)
        for ingredient in ingredients:
            print('\t',ingredient)

# printAllergens()

ingredientsWithAllergens = set()
for ingredients in allergenDict.values():
    ingredientsWithAllergens.update(ingredients)

occurence = 0

for ingredients,_ in foods:
    for ingredient in ingredients:
        if not ingredient in ingredientsWithAllergens:
            occurence += 1

print('Part 1:\n',occurence)

clearedAllergens = []
nextAllergen = next((allergen for allergen in allergenDict.keys() if (len(allergenDict[allergen]) == 1 and allergen not in clearedAllergens)),None)
while nextAllergen:

    for allergen in allergenDict.keys():
        if allergen == nextAllergen:
            continue
        allergenDict[allergen] -= allergenDict[nextAllergen]
        clearedAllergens.append(nextAllergen)

    nextAllergen = next((allergen for allergen in allergenDict.keys() if (len(allergenDict[allergen]) == 1 and allergen not in clearedAllergens)),None)

neatList = {key:list(value)[0] for (key,value) in allergenDict.items()}

allergenList = list(allergenDict.keys())

allergenList.sort()

print('Part 2:')
for i,allergen in enumerate(allergenList):
    if i != 0:
        print(',',end='')
    print(neatList[allergen],end='')
print()