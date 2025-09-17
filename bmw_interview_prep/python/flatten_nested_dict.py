'''
Write a function to flatten a deeply nested dictionary.

Input: {'a': {'b': {'c': 1}}, 'd': 2}
Output: {'a.b.c': 1, 'd': 2}

'''

def check_nested(test, output_dict = "", result = {}):
    if test:
        for key in test:
            if isinstance(test[key], dict):
                check_nested(test[key], output_dict+f"{key}.", result)
            else:
                output_dict += key
                result[output_dict] = test[key]
        return result



def solution(test):
    print(check_nested(test))


if __name__ == "__main__":
    test_case = {'a': {'b': {'c': 1}}, 'd': 2}
    solution(test_case)