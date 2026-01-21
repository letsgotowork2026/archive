n, m = map(int, input().split())

dna = []
for i in range(n):
    dna.append(input().strip())

ACGT = [[0]*4 for _ in range(m)]

for j in range(m):
    for i in range(n):
        if(dna[i][j] == 'A'):
            ACGT[j][0]+= 1
        elif dna[i][j] == 'C':
            ACGT[j][1] += 1
        elif dna[i][j] == 'G':
            ACGT[j][2] += 1
        elif dna[i][j] == 'T':
            ACGT[j][3] += 1

ans =[]
num = 0

for i in range(m):
    maxindex = 0
    for j in range(1, 4):
        if ACGT[i][j] > ACGT[i][maxindex]:
            maxindex = j
    if maxindex == 0:
        tmp = 'A'
    elif maxindex == 1:
        tmp = 'C'
    elif maxindex == 2:
        tmp = 'G'
    elif maxindex == 3:
        tmp = 'T'
    num += n - ACGT[i][maxindex] 
    ans.append(tmp)

print("".join(ans))
print(num)


