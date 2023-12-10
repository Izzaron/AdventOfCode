from math import ceil
from collections import Counter

def buy(item,amount,thingsToBuy,priceList):
    amountPerBuy = priceList[item][0]
    nrOfBuys = int(ceil(amount/amountPerBuy))
    thingsToBuy[item] -= amountPerBuy * nrOfBuys
    # if amountPerBuy * nrOfBuys != amount:
    #     print('Uneven buy of {}. Needed {}, bought {}.'.format(item,amount,amountPerBuy * nrOfBuys),end=' ')
    #     for costItem in priceList[item][1]:
    #         print('Costing {} {}'.format(nrOfBuys * costItem[1],costItem[0]),end=' ')
    #         # print('Wasting {} {}'.format((amountPerBuy * nrOfBuys - amount)/amountPerBuy * costItem[1],costItem[0]),end=' ')
    #     print()
    for costItem in priceList[item][1]:
        thingsToBuy[costItem[0]] += nrOfBuys * costItem[1]

def main(inputFile):
    puzzleInput = open(inputFile)

    priceList = dict()
    for row in puzzleInput:
        rawMaterials,product = row.split('=>')
        rawMaterials = rawMaterials.split(',')
        materials = []
        for material in rawMaterials:
            material = material.split()
            materials.append((material[1],int(material[0])))
        product = product.split()
        # product = (product[1],int(product[0]))
        priceList[product[1]] = (int(product[0]),materials)
        # print(materials,':',product)
    
    # for key,item in priceList.items():
    #     print(key,item)

    thingsToBuy = Counter()
    fuelBought = 1
    thingsToBuy['FUEL'] = 1
    nextUpdate = 10
    while(True):
        while(any([amount > 0 for item,amount in thingsToBuy.items() if item != 'ORE'])):
            temporaryShoppingList = Counter()
            for item,amount in thingsToBuy.items():
                if item == 'ORE':
                    continue
                if amount > 0:
                    buy(item,amount,temporaryShoppingList,priceList)
            # thingsToBuy += temporaryShoppingList
            thingsToBuy.update(temporaryShoppingList)
        if thingsToBuy['ORE'] > 1000000000000:
            break
        elif thingsToBuy['ORE'] > nextUpdate:
            print(thingsToBuy['ORE'])
            nextUpdate *= 10
        fuelBought += 1
        thingsToBuy['FUEL'] += 1
    
        # print(*['{}:{}\n'.format(k,v) for k,v in thingsToBuy.items()],end='')
    # return thingsToBuy['ORE']
    return fuelBought
    # print(*['{}:{}\n'.format(k,v) for k,v in priceList.items()])


if __name__ == '__main__':
    # ans1 = main('input14test1.txt')
    # print(ans1==31)
    # ans2 = main('input14test2.txt')
    # print(ans2==165)
    # ans3 = main('input14test3.txt')
    # print(ans3==13312)
    # ans4 = main('input14test4.txt')
    # print(ans4==180697)
    # ans5 = main('input14test5.txt')
    # print(ans5==2210736)
    # ans = main('input14.txt')
    # print(ans<374126,':',ans)

    # part 2
    # ans3 = main('input14test3.txt')
    # print(ans3)
    # ans4 = main('input14test4.txt')
    # print(ans4)
    ans5 = main('input14test5.txt')
    print(ans5)
    ans = main('input14.txt')
    print(ans)