import random
from typing import List

def find_min_max(array: List[int]):
    if len(array) == 0:
        return None

    if len(array) == 1:
        return array[0], array[0]

    mid = len(array) // 2
    left_min, left_max = find_min_max(array[:mid])
    right_min, right_max = find_min_max(array[mid:])

    return min(left_min, right_min), max(left_max, right_max)

if __name__ == "__main__":
    array = [random.randint(1, 100) for _ in range(20)]

    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_value, max_value = find_min_max(array)
    print(f"Мінімум: {min_value}, Максимум: {max_value}")
