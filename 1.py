def get_median_word(self, text: str) -> str:
    half_length = len(text) // 2
    return text[half_length] if len(text) % 2 != 0 else text[half_length - 1 : half_length + 1]
