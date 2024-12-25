m, n = map(int, input().split())

numdict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

answer = []
for x in range(m, n+1):
    y = ' '.join([numdict[z] for z in str(x)])
    answer.append([x, y])
    
answer.sort(key=lambda x:x[1])

for i in range(len(answer)):
    if i%10 == 0 and i!= 0:
        print()
    print(answer[i][0], end=' ')