from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com"

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def wait_for(driver, by, selector, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )

def login(driver, usuario, senha):
    driver.get(URL)
    wait_for(driver, By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(senha)
    driver.find_element(By.ID, "login-button").click()

# -------------------------------------------------------
# Contexto
# -------------------------------------------------------

@given("que o usuário acessa o site do SauceDemo")
def step_acessa_site(context):
    context.driver = get_driver()
    context.driver.get(URL)

@given("que o usuário está logado")
def step_usuario_logado(context):
    context.driver = get_driver()
    login(context.driver, "standard_user", "secret_sauce")

@given("adicionou um produto ao carrinho")
def step_adicionou_produto(context):
    wait_for(context.driver, By.CLASS_NAME, "btn_inventory")
    context.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

# -------------------------------------------------------
# Login
# -------------------------------------------------------

@when('preenche o usuário "{usuario}" e a senha "{senha}"')
def step_preenche_credenciais(context, usuario, senha):
    wait_for(context.driver, By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)

@when("clica em Login")
def step_clica_login(context):
    context.driver.find_element(By.ID, "login-button").click()

@then("é redirecionado para a página de inventário")
def step_pagina_inventario(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()

@then("uma mensagem de erro é exibida")
def step_mensagem_erro(context):
    erro = wait_for(context.driver, By.CLASS_NAME, "error-message-container")
    assert erro.is_displayed()
    context.driver.quit()

# -------------------------------------------------------
# Carrinho
# -------------------------------------------------------

@when("adiciona o primeiro produto ao carrinho")
def step_adiciona_produto(context):
    wait_for(context.driver, By.CLASS_NAME, "btn_inventory")
    context.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

@then("o carrinho exibe 1 item")
def step_carrinho_um_item(context):
    badge = wait_for(context.driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"
    context.driver.quit()

@when("acessa o carrinho e remove o produto")
def step_remove_produto(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(context.driver, By.CLASS_NAME, "cart_button")
    context.driver.find_element(By.CLASS_NAME, "cart_button").click()

@then("o carrinho fica vazio")
def step_carrinho_vazio(context):
    badges = context.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0
    context.driver.quit()

# -------------------------------------------------------
# Checkout
# -------------------------------------------------------

@when('finaliza o checkout com nome "{nome}" sobrenome "{sobrenome}" e CEP "{cep}"')
def step_checkout_completo(context, nome, sobrenome, cep):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(context.driver, By.ID, "checkout").click()
    wait_for(context.driver, By.ID, "first-name").send_keys(nome)
    context.driver.find_element(By.ID, "last-name").send_keys(sobrenome)
    context.driver.find_element(By.ID, "postal-code").send_keys(cep)
    wait_for(context.driver, By.ID, "continue").click()
    wait_for(context.driver, By.ID, "finish").click()

@then("a mensagem de confirmação é exibida")
def step_confirmacao(context):
    msg = wait_for(context.driver, By.CLASS_NAME, "complete-header")
    assert "Thank you" in msg.text
    context.driver.quit()

@when("tenta finalizar o checkout sem preencher os campos")
def step_checkout_sem_campos(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(context.driver, By.ID, "checkout").click()
    context.driver.find_element(By.ID, "continue").click()

@then("o carrinho exibe {quantidade} item")
def step_carrinho_quantidade(context, quantidade):
    badge = wait_for(context.driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == quantidade
    context.driver.quit()