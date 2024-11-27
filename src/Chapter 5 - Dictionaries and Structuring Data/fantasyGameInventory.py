def addToInventory(inventory, addedItems) -> dict:
    for i in range(len(addedItems) - 1):
        if inventory.get(addedItems[i]) is None:
            inventory[addedItems[i]] = 1
        else:
            inventory[addedItems[i]] += 1

    return inventory

def displayInventory(invent):
    print('Inventory: ')
    for item in invent:
        print(invent[item], item)
    print('Total number of items: ' + str(sum(invent.values())))

Inventory = {
    'gold coin': 42, 'rope': 1
}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Inventory = addToInventory(Inventory, dragonLoot)

displayInventory(Inventory)