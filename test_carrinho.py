"""Testes BDD para as regras de negócio do carrinho."""

from pathlib import Path

from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto


FEATURE_FILE = Path(__file__).parent / "carrinho.feature"
scenarios(str(FEATURE_FILE))


@given("que meu carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()


@given(
    parsers.parse("que há {estoque:d} unidades disponíveis em estoque"),
    target_fixture="estoque_disponivel",
)
def definir_estoque(estoque):
    return estoque


@when(
    parsers.parse(
        "adiciono {quantidade:d} unidades de um produto que custa {preco:f}"
    )
)
def adicionar_com_sucesso(carrinho, estoque_disponivel, quantidade, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque_disponivel, preco)
    except ValueError as erro:
        carrinho["erro"] = str(erro)


@when(
    parsers.parse(
        "tento adicionar {quantidade:d} unidades de um produto que custa {preco:f}"
    )
)
def tentar_adicionar_sem_estoque(
    carrinho, estoque_disponivel, quantidade, preco
):
    try:
        adicionar_produto(carrinho, quantidade, estoque_disponivel, preco)
    except ValueError as erro:
        carrinho["erro"] = str(erro)


@then(parsers.parse("o carrinho deve conter {quantidade:d} unidades"))
def validar_quantidade(carrinho, quantidade):
    assert carrinho["itens"] == quantidade


@then(parsers.parse("o valor total do carrinho deve ser {total:f}"))
def validar_total(carrinho, total):
    assert round(carrinho["total"], 2) == round(total, 2)


@then(parsers.parse('deve ocorrer o erro "{mensagem}"'))
def validar_erro(carrinho, mensagem):
    assert carrinho.get("erro") == mensagem


@then(parsers.parse("o carrinho deve continuar com {quantidade:d} unidades"))
def validar_quantidade_apos_falha(carrinho, quantidade):
    assert carrinho["itens"] == quantidade

