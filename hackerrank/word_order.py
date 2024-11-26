from collections import Counter
if __name__ == "__main__":
    number = int(input())
    list_words = list()
    for i in range(number):
        word = input()
        list_words.append(word)
    
    result = Counter(list_words)
    print(len(result.keys()))
    [print(result[data], end=" ") for data in result] 
