def fibonacci(n):
    """Genera una lista con la secuencia de Fibonacci hasta n términos."""
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

if __name__ == "__main__":
    n = int(input("¿Cuántos términos de Fibonacci quieres ver? "))
    print(f"Secuencia de Fibonacci ({n} términos):")
    print(fibonacci(n))