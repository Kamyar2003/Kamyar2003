def get_median_word(text: str) -> str:
    half_length = len(text) // 2
    return text[half_length] if len(text) % 2 != 0 else text[half_length - 1 : half_length + 1]


print(get_median_word("Python")) # th
print(get_median_word("Hello")) # l
