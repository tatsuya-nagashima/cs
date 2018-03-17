# coding=utf-8
#再帰


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def hanoi(N, src, work, dst):
    if N > 0:
        hanoi(N-1, src, dst, work)
        print ("move disk" + str(N) + " from " + str(src) + " to " + str(work))
        hanoi(N-1, dst, work, src)


if __name__ == "__main__":
    print ("Input number :"),
    n=int(raw_input())

    print ( "factorial : " + str(factorial(n)) )
    print ( "fibonacci : " + str(fibonacci(n)) )
    for i in range(n+1):
        a = fibonacci(i)
        print a,
    print "\n"

    print ("hanoi")
    hanoi(3,"A","B","C")
