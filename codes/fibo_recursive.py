def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

    
x = int(input('Position in fibonacci sequence: '))

res = fibonacci(x - 1)

print(f'The {x}° number in fibonacci sequence is: {res}')
