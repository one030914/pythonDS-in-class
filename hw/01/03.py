text = input()
n = int(input())

for i in range(n):
    cmd = input().split()
    cmd = [int(_) if _.isdigit() else _ for _ in cmd]
    if cmd[1] > cmd[2]:
        cmd[2], cmd[1] = cmd[1], cmd[2]
    if cmd[0] == "replace":
        text = text[:cmd[1]] + cmd[3][:cmd[2] - cmd[1] + 1] + text[cmd[2] + 1:]
    elif cmd[0] == "reverse":
        text = text[:cmd[1]] + text[cmd[1]:cmd[2] + 1][::-1] + text[cmd[2] + 1:]
    elif cmd[0] == "print":
        print(text[cmd[1]:cmd[2] + 1])