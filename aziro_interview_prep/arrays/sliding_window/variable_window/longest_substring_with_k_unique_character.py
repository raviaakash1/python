import math

def longest_substring_k_unique(s, k):
    start = 0
    max_len = 0
    char_freq = {}

    for end in range(len(s)):
        char_freq[s[end]] = char_freq.get(s[end], 0) + 1

        while len(char_freq) > k:
            char_freq[s[start]] -= 1
            if char_freq[s[start]] == 0:
                del char_freq[s[start]]
            start += 1

        if len(char_freq) == k:
            max_len = max(max_len, end - start + 1)

    return max_len if max_len != 0 else -1



if __name__ == "__main__":
    string = input()
    unique_characters = int(input())

    print(find_longest_substring_with_k_unique_characters(string, unique_characters))