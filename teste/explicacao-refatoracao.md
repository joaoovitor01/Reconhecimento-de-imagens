# Guia de Refatoração: Boas Práticas de Legibilidade e Nomenclatura

## Introdução

Refatoração é o processo de melhorar o código interno sem alterar seu comportamento externo. Este guia foca em boas práticas para aumentar a legibilidade e usar nomenclatura adequada, especialmente em Python.

## Princípios Gerais de Legibilidade

### 1. Código Limpo e Organizado

- Use indentação consistente (4 espaços em Python).
- Limite linhas a 79-88 caracteres.
- Separe seções lógicas com linhas em branco.

### 2. Nomenclatura Clara

- **Variáveis**: Use nomes descritivos em snake_case (ex: `numero_primo` em vez de `n`).
- **Funções**: Verbos descritivos (ex: `verificar_primalidade`).
- **Classes**: PascalCase (ex: `VerificadorPrimo`).
- **Constantes**: MAIÚSCULAS_COM_UNDERSCORE (ex: `LIMITE_MAXIMO`).

### 3. Comentários e Docstrings

- Use docstrings para funções e classes (formato Google ou NumPy).
- Comentários explicativos para lógica complexa.
- Evite comentários óbvios.

## Exemplos de Refatoração

### Antes (Código Original)

```python
def p(n):
    if n<2: return False
    for i in range(2,n):
        if n%i==0: return False
    return True
```

### Depois (Refatorado)

```python
def is_prime(number: int) -> bool:
    """Verifica se um número é primo.

    Args:
        number (int): O número a ser verificado.

    Returns:
        bool: True se primo, False caso contrário.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(number ** 0.5)
    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False
    return True
```

### Melhorias Aplicadas

- **Nomenclatura**: `p` → `is_prime`, `n` → `number`, `i` → `divisor`.
- **Legibilidade**: Adicionados casos especiais e docstring.
- **Eficiência**: Otimizado loop para divisores ímpares.

## Ferramentas de Apoio

- **Linters**: flake8, pylint para detectar problemas.
- **Formatters**: black para formatação automática.
- **IDE**: Use recursos de refatoração (renomear, extrair função).

## Conclusão

Aplicar essas práticas torna o código mais fácil de entender, manter e colaborar. Refatore incrementalmente, testando sempre para garantir funcionalidade.
