"""Add an item to the end of a list."""


def add_item(items, item):
    """Return the list with the item added at the end.

    Args:
        items: The list to add the item to.
        item: The item to append.

    Returns:
        The list with the item added at the end.
    """
    items.append(item)
    return items


# Test the function with different lists.
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
