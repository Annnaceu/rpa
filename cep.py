from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempoEspera.sleep(4)

# Preenche o CEP
navegador.find_element(By.NAME, "endereco").send_keys("27336580")
tempoEspera.sleep(2)

# Pausa para permitir inserção manual do CAPTCHA
input("Por favor, insira o CAPTCHA manualmente e pressione Enter para continuar...")

# Clique no botão de pesquisa
navegador.find_element(By.NAME, "btn_pesquisar").click()
tempoEspera.sleep(6)


