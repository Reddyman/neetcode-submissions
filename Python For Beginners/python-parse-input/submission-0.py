from typing import List

def read_integers() -> List[int]:
    integers = input("")
    return [int(i) for i in integers.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
