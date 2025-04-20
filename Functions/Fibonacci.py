def fibonacci(n):
    if n < 0:
        print("Not a valid input range")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]

    elif n > 2:
        Fibonacci = [0,1]
        for i in range(1,n-1):
            Fibonacci.append(Fibonacci[i] + Fibonacci[i-1])

        return Fibonacci