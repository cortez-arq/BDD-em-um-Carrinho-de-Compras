"""Regras de negócio do carrinho de compras."""


def criar_carrinho():
    """Cria e retorna um carrinho vazio."""
    return {"total": 0.0, "itens": 0}


def adicionar_produto(
    carrinho,
    quantidade_desejada,
    estoque_disponivel,
    preco_unitario,
):
    """Adiciona produtos se houver estoque suficiente."""
    if quantidade_desejada <= 0:
        raise ValueError("A quantidade desejada deve ser positiva.")

    if preco_unitario < 0:
        raise ValueError("O preço unitário não pode ser negativo.")

    if quantidade_desejada > estoque_disponivel:
        raise ValueError("Estoque insuficiente")

    carrinho["itens"] += quantidade_desejada
    carrinho["total"] += quantidade_desejada * preco_unitario

    return carrinho

