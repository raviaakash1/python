def backtrack(arr, index, target, sum):
    if target == sum:
        return 1
    if sum > target:
        return 0
    if index >= len(arr):
        return 0
    sum = sum + arr[index]    
    pick = backtrack(arr, index + 1, target, sum )
    sum = sum - arr[index]    
    not_pick = backtrack(arr, index + 1, target, sum)
    return pick + not_pick
    

if __name__ == "__main__":
    arr = [5, 4, 9]
    target = 9
    counter = 0
    print(backtrack(arr, 0, target, 0))
    