'''
Write a function to flatten a deeply nested dictionary.

Input: {'a': {'b': {'c': 1}}, 'd': 2}
Output: {'a.b.c': 1, 'd': 2}

'''

def flatten_dict(d, parent_key='', result=None):
    if result is None:
        result = {}
    for k, v in d.items():
        full_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            flatten_dict(v, full_key, result)
        else:
            result[full_key] = v
    return result

def solution(test_case):
    flattened = flatten_dict(test_case)
    print(flattened)

if __name__ == "__main__":
    test_case = {
        "a": 1,
        "b": {
            "c": 2,
            "d": {
                "e": 3
            }
        }
    }
    solution(test_case)