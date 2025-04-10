k = int(input())
n = int(input())
datasets = []

def isNumeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
for _ in range(n):
    datasets.append([float(_) if isNumeric(_) else _ for _ in input().split(sep=",")])

m = int(input())

for _ in range(m):
    test = [float(_) for _ in input().split(sep=",")]
    distances = []
    ans = {}
    
    for i in range(len(datasets)):
        subtract = []
        for j in range(len(datasets[i]) - 1):
            subtract.append(datasets[i][j] - test[j])
            ans[datasets[i][-1]] = 0
        distances.append((datasets[i][-1], pow(sum(map(lambda x: x * x, subtract)), 0.5)))
    
    for data in sorted(distances, key=lambda x: x[1])[:k]:
        ans[data[0]] += 1
    
    print(max(ans, key=ans.get))
