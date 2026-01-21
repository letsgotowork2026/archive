from collections import deque

n = int(input())
queue = deque()

cmd_with_param = ['push_back', 'push_front']

for i in range(n):
    # print("#",i)
    input_list = list(input().split(' '))

    if len(input_list) == 2:
        command = input_list[0]
        parameter = int(input_list[1])

        if command == 'push_back':
            queue.append(parameter)
        else:
            queue.appendleft(parameter)

        
    else : 
        command = input_list[0]
        
        if command == 'pop_front':
            if queue.__len__() == 0:
                print(-1)
            else:
                print(queue.popleft()) 
        elif command == 'pop_back':
            if queue.__len__() == 0:
                print(-1)
            else:
                print(queue.pop())
        elif command == 'size':
            print(queue.__len__())
        elif command == 'empty':
            if queue.__len__() == 0:
                print(1)
            else:
                print(0)
        elif command == 'front':
            if queue.__len__() == 0:
                print(-1)
            else:
                print(queue[0])
        elif command == 'back':
            if queue.__len__() == 0:
                print(-1)
            else:
                print(queue[-1])
    
    # print(queue)
    # print("--------")

