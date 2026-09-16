from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char_count = {}
    for c in word:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
