'''
Default Dict :: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
'''
inputed = input().split(" ")
n = int(inputed[0])
m = int(inputed[1])
listed = list()
for i in range(n):
    inputed = input()
    listed.append(str(inputed))

to_check = list()
for i in range(m):
    inputed = input()
    to_check.append(str(inputed))

for str_to_check in to_check:
    for index, data in enumerate(listed):
        if str_to_check == data:
            print(index + 1, end=" ")
    print()


