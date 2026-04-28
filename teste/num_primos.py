def is_prime(n: int) -> bool:
    """Verifica se um número é primo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**0.5)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    examples = [0, 1, 2, 3, 4, 17, 18, 19, 20]
    for value in examples:
        print(f"{value}: {is_prime(value)}")