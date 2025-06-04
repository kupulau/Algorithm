n = int(input())
gene = list(input().strip())

table = {
    ('A', 'A'): 'A',
    ('A', 'G'): 'C',
    ('A', 'C'): 'A',
    ('A', 'T'): 'G',
    ('G', 'A'): 'C',
    ('G', 'G'): 'G',
    ('G', 'C'): 'T',
    ('G', 'T'): 'A',
    ('C', 'A'): 'A',
    ('C', 'G'): 'T',
    ('C', 'C'): 'C',
    ('C', 'T'): 'G',
    ('T', 'A'): 'G',
    ('T', 'G'): 'A',
    ('T', 'C'): 'G',
    ('T', 'T'): 'T'
}

while len(gene) > 1:
    a = gene.pop()
    b = gene.pop()
    gene.append(table[(b, a)])

print(gene[0])
