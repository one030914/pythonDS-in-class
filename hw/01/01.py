while True:
    try:
        line = input()
        nums = line.split()
        num = sum([int(_) for _ in nums])
        print(len(list(str(num))))
    except EOFError:
        break
