"""Iterator that splits any iterable into batches of a fixed size."""


class Batches:
    """Iterate over an iterable in lists of ``size`` elements.

    The elements are read lazily from the source iterable. The last batch
    may be shorter than ``size``.

    Attributes:
        size: Number of elements in one batch.
    """

    def __init__(self, items, size):
        """Store the source iterator and the batch size.

        Args:
            items: Any iterable (list, tuple, string, generator, ...).
            size: Number of elements in one batch, a positive integer.

        Raises:
            TypeError: If ``size`` is not an integer or ``items`` is not
                iterable.
            ValueError: If ``size`` is smaller than 1.
        """
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError(
                f"size must be an integer, got {type(size).__name__}"
            )
        if size < 1:
            raise ValueError(f"size must be at least 1, got {size}")
        try:
            self._items = iter(items)
        except TypeError as error:
            raise TypeError(
                f"items must be iterable, got {type(items).__name__}"
            ) from error
        self.size = size

    def __iter__(self):
        """Return the iterator itself.

        Returns:
            This ``Batches`` object.
        """
        return self

    def __next__(self):
        """Return the next batch.

        Returns:
            A list with up to ``size`` elements.

        Raises:
            StopIteration: If there are no elements left.
        """
        batch = []
        for item in self._items:
            batch.append(item)
            if len(batch) == self.size:
                break
        if not batch:
            raise StopIteration
        return batch
