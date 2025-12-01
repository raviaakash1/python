"""
given 2 string

str1[] : "foaxxorfxaofr"
str2[] : "fox"

anagram : can jumblee the words
    example : "for"
               anagrams : "rof"
                         : "fro"
                          etc...

"""

def create_hash_map(sub_string):
    hash_map = dict()
    for char in sub_string:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    return hash_map

def count_anagrams(string, sub_string):
    sliding_window = len(sub_string)
    hash_map = create_hash_map(sub_string)

    start = 0
    end = 0
    result = 0
    char_parsed = {i :0 for i in sub_string}
    
    while end < len(string):
        if string[end] in hash_map.keys():
            char_parsed[string[end]] += 1
        if end-start+1 < sliding_window:
            end += 1
        elif end - start + 1 == sliding_window:
            if char_parsed == hash_map:
                char_parsed[string[start]] -= 1
                result += 1
            else:
                if string[start] in char_parsed.keys():
                    char_parsed[string[start]] -= 1
            start += 1
            end += 1
    return result
            
if __name__ == "__main__":
    main_string = input("Enter a string : ")
    sub_string = input("Enter a substring : ")
    print(count_anagrams(main_string, sub_string))