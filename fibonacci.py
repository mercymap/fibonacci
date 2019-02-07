def fibonacci(n):
    if isinstance(n, int):
        if n == 0:
            return "fibonacci"
        if n == 1:
            return "fibonacci"
        if n == ((n - 2) + (n - 1)):
            return "fibonacci"
        return "not fibonacci"    
    raise ValueError("Invalid input")

n = 3
print(fibonacci(n))