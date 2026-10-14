"""Remove an item from a list."""


def remove_item(items, item):
    """Return the list with the given item removed.

    Args:
        items: The list to remove the item from.
        item: The item to remove.

    Returns:
        The list with the item removed.
    """
    items.remove(item)
    return items


# Test the function with different lists.
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
