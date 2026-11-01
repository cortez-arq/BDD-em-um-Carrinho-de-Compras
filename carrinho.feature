# language: pt

Funcionalidade: Carrinho de compras
  Como cliente de um e-commerce
  Quero adicionar produtos ao carrinho
  Para acompanhar o valor total da minha compra

  Cenário: Adicionar um produto com sucesso
    Dado que meu carrinho está vazio
    E que há 10 unidades disponíveis em estoque
    Quando adiciono 3 unidades de um produto que custa 25.00
    Então o carrinho deve conter 3 unidades
    E o valor total do carrinho deve ser 75.00

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Dado que meu carrinho está vazio
    E que há 2 unidades disponíveis em estoque
    Quando tento adicionar 5 unidades de um produto que custa 25.00
    Então deve ocorrer o erro "Estoque insuficiente"
    E o carrinho deve continuar com 0 unidades
    E o valor total do carrinho deve ser 0.00
