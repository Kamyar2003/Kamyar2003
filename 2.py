def to_1darray(array: list) -> list:
	""" This method is used to complete all `( n-Dimensional )` lists.
        This method takes a variety of data, such as
        Lists and Tuples, to access all of its values,
        inserts them into a new list, and finally returns them.

        Example
        -------
        >>> data = [[1, 2, 3], [4, 5, 6], [[[7, 8], 9]]]
        >>> print(to_1darray(data))
        Output:
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

        Or
        --
        >>> data = [['A', 'B', 'C'],
        >>>         ['D', 'E', 'F']]
        >>> print(to_1darray(data))
        Output:
        ['A', 'B', 'C', 'D', 'E', 'F']
    """

    complete_list = []

    def into_complete(array_into: list) -> list:
        for arr in array_into:
            if isinstance(arr, list):
                into_complete(arr)
                continue
            complete_list.append(arr)
        return complete_list

    return into_complete(array)


# test

data = [[1, 2, 3], [4, 5, 6], [[[7, 8], 9]]]
print(to_1darray(data))


data = [['A', 'B', 'C'],
        ['D', 'E', 'F']]
print(to_1darray(data))






