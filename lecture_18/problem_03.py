import json


def char_with_max_occurrences(string: str) -> str:
    d = {}

    for char in string:
        if d.get(char) is None:
            d[char] = 0

        d[char] += 1

    current_max_occurences = 0
    current_max_char = "a"

    for char in d:
        if current_max_occurences < d[char]:
            current_max_occurences = d[char]
            current_max_char = char

    return current_max_char


if __name__ == '__main__':
    print("the char is: '", char_with_max_occurrences("this is a very boring sentence... Don't you think so! aa"), "'")  # A space - has 10 occurrences
