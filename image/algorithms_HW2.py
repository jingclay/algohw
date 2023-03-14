string_1 = "kxreddddt"


def split_swap(value):
    length_of_value = len(value)
    length_of_shorter_half = length_of_value // 2
    length_of_longer_half = length_of_value - length_of_shorter_half

    first_half_of_value = value[:length_of_longer_half]
    last_half_of_value = value[length_of_longer_half:]

    return last_half_of_value + first_half_of_value


print(len(string_1))
print(string_1)
print(split_swap(string_1))


def unique_character(value):
    return len(value) == len(set(value))


print(unique_character("abc"))
print(unique_character("aab"))

