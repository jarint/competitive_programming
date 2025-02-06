import fileinput

ops = []
for line in fileinput.input():
    line = line.strip()
    num1, operation, num2 = line.split()
    num1 = int(num1)
    num2 = int(num2)
    ops.append((num1, operation, num2))

def calc(tup):
    n1 = tup[0]
    op = tup[1]
    n2 = tup[2]

    match op:
        case '+':
            result = n1 + n2
        case '*':
            result = n1 * n2
        case '^':
            result = pow(n1, n2, 10000)

    return result % 10000

for op in ops:
    answer = calc(op)
    print(str(answer).lstrip("0") or "0")