def sort_asc(tuple_numbers: tuple) -> list:
    sorted_numbers = sorted(list(tuple_numbers))
    print(sorted_numbers)
    return sorted_numbers


def sort_desc(tuple_numbers: tuple) -> list:
    sorted_numbers = sorted(list(tuple_numbers), reverse=True)
    print(sorted_numbers)
    return sorted_numbers


def sort_words(tuple_words: tuple) -> list:
    sorted_words = sorted(list(tuple_words), key=len)
    print(sorted_words)
    return sorted_words


random_numbers = (3, 764, 8, 12, 45, 111, 678, 267, 33)
random_words = ('banana', 'boy', 'apple', 'home', 'work')

sort_asc(tuple_numbers=random_numbers)
sort_desc(tuple_numbers=random_numbers)
sort_words(tuple_words=random_words)
