def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2

    >>> count_vowels('Manila')
    3

    >>> count_vowels('Istanbul')
    3
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels


def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    """
    return a + b


def mul(a, b):
    """
    Given two integers, return the mul.

    :param a: int
    :param b: int
    :return: int

    >>> mul(3, 3)
    9
    """
    return a * b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
