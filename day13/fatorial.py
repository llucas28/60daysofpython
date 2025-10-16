def fatorial (n):
    """
Calcula o fatorial de um número usando recursão.

:parametro n: Numero inteiro não negativo
:return: Fatorial de n.
    """
    if n < 0:
        raise ValueError("O número deve ser positivo")
    
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial(n-1)

print(fatorial(2))

try:
    print(f"Fatorial igual a {fatorial(1)}")
except ValueError as e:
    print(e)