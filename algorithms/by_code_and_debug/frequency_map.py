from typing import List, Dict

def get_frequency(data: List[int]) -> Dict[int, int]:
    result: Dict[int, int] = {}
    for key in data:
        result[key] = result.get(key, 0) + 1 # looks up key if present returns its value else assign 0 as default value
    return result


if __name__ == "__main__":
    data: List[int] = [int(i) for i in input("Enter list of numbers >> ").split(' ')]
    print(get_frequency(data))