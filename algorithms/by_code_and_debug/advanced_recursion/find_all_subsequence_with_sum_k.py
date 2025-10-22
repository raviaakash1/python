
result = []

def backtrack(arr, target, subset, index, sum):
    if target == sum:
        result.append(subset.copy())
        return
    if sum > target :
        return
    if index >= len(arr):
        return
    subset.append(arr[index])
    sum = sum + arr[index]
    backtrack(arr, target, subset, index + 1, sum)
    subset.pop()
    sum = sum - arr[index]
    backtrack(arr, target, subset, index + 1, sum)

if __name__ == "__main__":
    arr = [5, 4, 9]
    target = 9
    backtrack(arr, target, [], 0, 0)
    print(result)