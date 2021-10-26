#递归
def hanro(n):
    return move(n, 1)

def move(n, num):
    if n == 1:
        return num
    return move(n - 1, num * 2 + 1)
