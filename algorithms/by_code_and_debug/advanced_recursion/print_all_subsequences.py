result = []
def solve(index, subset, arr):
    if index >= len(arr):
        result.append(subset.copy())
        return
    subset.append(arr[index])
    solve(index + 1, subset, arr)
    subset.pop()
    solve(index + 1, subset, arr)

if __name__ == "__main__":
    arr = [5, 7, 9]
    solve(0, [], arr)
    print(result)