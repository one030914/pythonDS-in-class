n = int(input())

for _ in range(n):
    n1 = int(input())
    n2 = int(input())
    n3 = n1 + n2
    if(len(str(n3)) > 80):
        print("overflow")
    else:
        print(n3)