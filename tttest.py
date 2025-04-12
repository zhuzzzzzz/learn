import sys

line = input()
print(line)
# get []
while True:
    left_pos = -1
    right_pos = -1
    length = len(line)
    for i in range(length - 1, -1, -1):
        cha = line[i]
        if cha == "[":
            left_pos = i
            break
    if left_pos == -1:
        break
    for j in range(left_pos + 1, length):
        cha = line[left_pos]
        if cha == "]":
            right_pos = j
            break
    if left_pos !=-1 and right_pos != -1 and right_pos > left_pos:
        get_expression = line[left_pos+1:right_pos]
        print(get_expression)
        val = eval(get_expression)
        print(line)
        line = f'{line[0:left_pos]}' + f'{val}' + f'{line[right_pos + 1:]}'
    else:
        break

# get {}
while True:
    left_pos = -1
    right_pos = -1
    length = len(line)
    for i in range(length - 1, -1, -1):
        cha = line[i]
        if cha == "{":
            left_pos = i
            break
    if left_pos == -1:
        break
    for j in range(left_pos + 1, length):
        cha = line[left_pos]
        if cha == "}":
            right_pos = j
            break
    if left_pos !=-1 and right_pos != -1 and right_pos > left_pos:
        get_expression = line[left_pos+1:right_pos]
        print(get_expression)
        val = eval(get_expression)
        print(line)
        line = f'{line[0:left_pos]}' + f'{val}' + f'{line[right_pos + 1:]}'
    else:
        break

print(eval(line))
