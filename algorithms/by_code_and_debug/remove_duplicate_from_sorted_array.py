from typing import List

def remove_dups(list_nums: List[int]) -> List[int]:
    result: List[int] = ["-inf"]*(len(list_nums))
    res_index: int = int(-1)
    for num in list_nums:
        if result[res_index] == num and res_index != -1:
            continue
        else:
            res_index += 1
            result[res_index] = num
    return result
if __name__ == "__main__":
    list_nums: List[int] = [int(i) for i in input("Enter sorted array >> ").split(" ")]
    resultant_array: List[int] = remove_dups(list_nums)
    print(resultant_array)