// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update

type InventoryItemSet = Array<[number, string]>;

function updateInventory(
  inventory: InventoryItemSet,
  updates: InventoryItemSet
) {
  updates.forEach(([updateQuantity, updateName]) => {
    let isInInventory = false;
    inventory.forEach(([itemQuantity, itemName], itemIndex) => {
      if (itemName === updateName) {
        inventory[itemIndex] = [itemQuantity + updateQuantity, updateName];
        isInInventory = true;
      }
    });

    if (!isInInventory) {
      inventory.push([updateQuantity, updateName]);
    }
  });

  return inventory.sort(([ax, aName], [bx, bName]) => {
    if (aName < bName) return -1;
    if (aName > bName) return 1;
    return 0;
  });
}

// Example inventory lists
const curInv: InventoryItemSet = [
  [21, "Bowling Ball"],
  [2, "Dirty Sock"],
  [1, "Hair Pin"],
  [5, "Microphone"],
];

const newInv: InventoryItemSet = [
  [2, "Hair Pin"],
  [3, "Half-Eaten Apple"],
  [67, "Bowling Ball"],
  [7, "Toothpaste"],
];

const t1 = updateInventory(curInv, newInv);

console.log(t1);
