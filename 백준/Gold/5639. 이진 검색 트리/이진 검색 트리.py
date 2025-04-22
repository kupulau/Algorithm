import sys
sys.setrecursionlimit(10**6)  
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break  # EOF

def make_tree(start, end):
    if start > end:
        return
    root = preorder[start]
    
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1

    make_tree(start + 1, idx - 1)
    make_tree(idx, end)
    print(root)

make_tree(0, len(preorder) - 1)