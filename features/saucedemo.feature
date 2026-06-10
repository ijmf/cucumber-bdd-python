# language: pt

Funcionalidade: SauceDemo — Fluxos principais
  Como usuário do SauceDemo
  Quero realizar compras na plataforma
  Para validar os fluxos de Login, Carrinho e Checkout

  Contexto:
    Dado que o usuário acessa o site do SauceDemo

  Cenário: Login com credenciais válidas
    Quando preenche o usuário "standard_user" e a senha "secret_sauce"
    E clica em Login
    Então é redirecionado para a página de inventário

  Cenário: Login com senha inválida
    Quando preenche o usuário "standard_user" e a senha "senha_errada"
    E clica em Login
    Então uma mensagem de erro é exibida

  Cenário: Login com usuário bloqueado
    Quando preenche o usuário "locked_out_user" e a senha "secret_sauce"
    E clica em Login
    Então uma mensagem de erro é exibida

  Cenário: Adicionar produto ao carrinho
    Dado que o usuário está logado
    Quando adiciona o primeiro produto ao carrinho
    Então o carrinho exibe 1 item

  Cenário: Remover produto do carrinho
    Dado que o usuário está logado
    E adicionou um produto ao carrinho
    Quando acessa o carrinho e remove o produto
    Então o carrinho fica vazio

  Cenário: Checkout completo com sucesso
    Dado que o usuário está logado
    E adicionou um produto ao carrinho
    Quando finaliza o checkout com nome "Ivan" sobrenome "Ferreira" e CEP "70000000"
    Então a mensagem de confirmação é exibida

  Cenário: Checkout sem preencher campos
    Dado que o usuário está logado
    E adicionou um produto ao carrinho
    Quando tenta finalizar o checkout sem preencher os campos
    Então uma mensagem de erro é exibida