import sys
import itertools


logic = {
    "p": 0, "q": 1, "r": 2, "s": 3, "t": 4
}


truth_assignments = list(itertools.product([0, 1], repeat=5))


while True:
    WFF = sys.stdin.readline().strip()


    if WFF == "0":
        break

    is_tautology = True


    for truth_values in truth_assignments:
        stack = list(WFF)
        eval = [truth_values[logic[stack.pop()]]]


        while stack:
            operator = stack.pop()

            if operator in logic:
                eval.append(truth_values[logic[operator]])
            else:
                if operator == 'K':
                    eval.append(eval.pop() & eval.pop())
                elif operator == 'A':
                    eval.append(eval.pop() | eval.pop())
                elif operator == 'N':
                    eval.append(1 - eval.pop())
                elif operator == 'C':
                    a, b = eval.pop(), eval.pop()
                    eval.append(1 if not a or b else 0)
                elif operator == 'E':
                    eval.append(1 if eval.pop() == eval.pop() else 0)

        if eval.pop() == 0:
            is_tautology = False
            break 

    print("tautology" if is_tautology else "not")
