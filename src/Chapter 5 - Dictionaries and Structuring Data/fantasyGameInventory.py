from operator import countOf

Inventory = {
    'rope': 12, 'torch': 6, 'gold coin': 4,
    'dagger': 3, 'arrow': 1
}

def displayInventory(invent):
    print('Inventory: ')
    for item in invent:
        print(invent[item], item)
    print('Total number of items: ' + str(sum(invent.values())))

displayInventory(Inventory)