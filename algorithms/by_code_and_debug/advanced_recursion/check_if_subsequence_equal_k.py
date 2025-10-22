

def solve(arr, index, target, sum):
    if target == sum:
        return True
    if sum > target:
        return False
    if index >= len(arr):
        return False
    sum = sum + arr[index]
    pick = solve(arr, index + 1, target, sum)
    if pick:
        return True
    sum = sum - arr[index]
    not_pick = solve(arr, index + 1, target, sum)
    return not_pick

if __name__ == "__main__":
    arr = [5, 4, 9]
    target = 9
    print(solve(arr, 0, target, 0))
