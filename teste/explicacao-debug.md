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

if **name** == "**main**":
examples = [0, 1, 2, 3, 4, 17, 18, 19, 20]
for value in examples:
print(f"{value}: {is_prime(value)}")

---

Linha 1: define a função `is_prime` que recebe um número inteiro `n` e retorna um valor booleano.

Linhas 2-10: docstring que descreve o objetivo da função, o parâmetro esperado e o valor de retorno.

Linha 11: verifica se `n` não é um inteiro; se não for, retorna `False` imediatamente.

Linha 12: a indentação dentro do `if` garante que a função termine e devolva `False` quando o valor não for inteiro.

Linha 13: verifica se `n` é menor ou igual a 1; números 0 e 1 não são primos.

Linha 14: retorna `False` quando `n` é 0 ou 1.

Linha 15: verifica se `n` é igual a 2; 2 é o menor número primo.

Linha 16: retorna `True` para `n == 2`.

Linha 17: verifica se `n` é par e maior que 2; nesse caso, não é primo.

Linha 18: retorna `False` quando `n` é um número par maior que 2.

Linha 20: calcula `limit` como a raiz quadrada de `n`, convertida em inteiro. Isso reduz os divisores que precisam ser testados.

Linha 21: inicia um loop sobre divisores ímpares de 3 até `limit`, inclusive.

Linha 22: dentro do loop, testa se `n` é divisível pelo divisor atual.

Linha 23: retorna `False` se encontrar um divisor exato, indicando que `n` não é primo.

Linha 24: se o laço terminar sem encontrar divisores, retorna `True`, confirmando que `n` é primo.

Linha 27: verifica se o arquivo está sendo executado diretamente (não importado como módulo).

Linha 28: define a lista `examples` com números usados para teste.

Linha 29: percorre cada valor na lista `examples`.

Linha 30: imprime o número e o resultado de `is_prime(value)` no formato `valor: True/False`.
