from timeit import timeit
from functools import lru_cache

def evaluateExpression(expression):
    start = timeit()
    ans = solve(expression, 0, len(expression) - 1);
    end = timeit()
    print(end - start)
    return ans

@lru_cache(None)
def solve(expression, i, j, bool = True):
    if i == j:
        if bool:
            return 1 if expression[i] == 'T' else 0
        else:
            return 1 if expression[i] == 'F' else 0


    temp = 0
    for k in range(i+1, j, 2):
        leftTrue = solve(expression, i, k - 1)
        rightTrue = solve(expression, k + 1, j)
        leftFalse = solve(expression, i, k - 1, False)
        rightFalse = solve(expression, k + 1, j, False)

        if expression[k] == '^':
            if bool:
                temp = temp + leftTrue * rightFalse + leftFalse * rightTrue
            else:
                temp = temp + leftTrue * rightTrue + rightFalse * leftFalse
        elif expression[k] == '|':
            if bool:
                temp = temp + leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse;
            else:
                temp = temp + leftFalse * rightFalse
        else:
            if bool:
                temp = temp + leftTrue * rightTrue
            else:
                temp = temp + leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse

    return temp


print(evaluateExpression('F&T|F|T'))
