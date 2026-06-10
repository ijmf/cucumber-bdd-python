# cucumber-bdd-python

Testes BDD automatizados com Behave e Selenium para o SauceDemo, cobrindo Login, Carrinho e Checkout em linguagem natural (português).

## O que é

Suite de testes end-to-end construída com Behave (Cucumber para Python) e Selenium WebDriver. Os cenários são escritos em Gherkin em português, tornando os testes legíveis para qualquer pessoa do time — desenvolvedores, analistas e stakeholders. O Chrome roda em modo headless.

## Stack

- Python 3.13
- Behave — framework BDD (Cucumber para Python)
- Selenium WebDriver — automação do browser
- WebDriver Manager — gerenciamento automático do ChromeDriver
- Gherkin em português — cenários legíveis por humanos

## Estrutura

```
cucumber-bdd-python/
├── features/
│   ├── saucedemo.feature    # 7 cenários em Gherkin (português)
│   └── steps/
│       └── saucedemo_steps.py  # Implementação dos steps
├── requirements.txt
└── .gitignore
```

## Como executar

```bash
# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar todos os testes
behave

# Rodar um cenário específico
behave --name "Login com credenciais válidas"
```

## Cenários

| Cenário | O que valida |
|---|---|
| Login com credenciais válidas | Redireciona para inventário após login |
| Login com senha inválida | Exibe mensagem de erro |
| Login com usuário bloqueado | Exibe mensagem de erro |
| Adicionar produto ao carrinho | Badge exibe 1 item |
| Remover produto do carrinho | Carrinho fica vazio |
| Checkout completo com sucesso | Exibe "Thank you for your order!" |
| Checkout sem preencher campos | Exibe mensagem de erro |

## Resultado

1 feature — 7 cenários — 31 steps — 0 falhas — 47s
