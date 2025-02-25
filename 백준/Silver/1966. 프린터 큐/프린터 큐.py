import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [[i, v] for i, v in enumerate(queue)]
    if len(queue)==1:
        print(1)    # queue with len 1 always have priority
    else:
        print1 = []
        while len(print1) < n:
            max1 = max([x[1] for x in queue])
            if queue[0][1] == max1:
                print1.append(queue[0])
                queue.pop(0)
            else:
                queue.append(queue.pop(0))
                
        answer = [x for x in print1 if x[0]==m][0]
        print(print1.index(answer)+1)