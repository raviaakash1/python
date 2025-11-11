def merge_sort(intervals):
    pass

def sort_two_d_list(intervals):
    
    merge_sort(intervals)


def remove_duplicates_2d(lst):
    seen = set()
    result = []
    for sublist in lst:
        t = tuple(sublist)
        if t not in seen:
            seen.add(t)
            result.append(sublist)
    return result


if __name__ == "__main__":
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))
    print(sorted(remove_duplicates_2d(intervals)))