from collections import deque

if __name__ == "__main__":
    commands = int(input())
    queue = deque()

    for _ in range(commands):
        command =  input()
        if command.find("popleft") != -1:
            queue.popleft()
        elif command.find("pop") != -1:
            queue.pop()
        elif command.find("appendleft") != -1:
            queue.appendleft(command.split(" ")[-1])
        elif command.find('append') != -1:
            queue.append(command.split(" ")[-1])

    [print(d, end = " ") for d in queue]