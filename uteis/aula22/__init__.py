def aumentar(preco, taxa):
    """Aumenta um preço em uma determinada porcentagem.

    Args:
        preco (float): O preço original.
        taxa (float): A taxa de aumento em percentual.

    Returns:
        float: O novo preço após o aumento.
    """
    porcentagem = preco * (taxa/100)
    return preco + porcentagem

def diminuir(preco, taxa):
    """Diminui um preço em uma determinada porcentagem.

    Args:
        preco (float): O preço original.
        taxa (float): A taxa de redução em percentual.

    Returns:
        float: O novo preço após a redução.
    """
    porcentagem = preco * (taxa/100)
    return preco - porcentagem

def dobro(preco):
    """Dobra o valor de um preço.

    Args:
        preco (float): O preço original.

    Returns:
        float: O dobro do preço.
    """
    return preco * 2

def metade(preco):
    """Calcula a metade de um preço.

    Args:
        preco (float): O preço original.

    Returns:
        float: A metade do preço.
    """
    return preco / 2