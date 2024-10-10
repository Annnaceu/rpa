from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

tempoEspera.sleep(5)
#prenche o campo nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Ana Maria")
tempoEspera.sleep(1)


#prenche o campo sobrenome
navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Gomes")
tempoEspera.sleep(1)

#prenche o campo email
navegador.find_element(By.NAME, "q4_email").send_keys("anamariadoceu@icloud.com")
tempoEspera.sleep(3)

#seleciona o campo estado civil
pegaDropDown = navegador.find_element(By.ID, "input_5")
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(1)
tempoEspera.sleep(2)

filho = "Não"
if filho == "Sim":
#Marca a opçao que tem\sim
    navegador.find_element(By.ID, "label_input_6_0").click()
else:
#Marca a opçao que tem\nao
    elemento_filho = navegador.find_element(By.ID, "label_input_6_1")
navegador.execute_script("arguments[0].scrollIntoView();", elemento_filho)
elemento_filho.click()

    #navegador.find_element(By.ID, "label_input_6_1").click()
tempoEspera.sleep(2)

#Marca a cor azul
navegador.find_element(By.ID, "label_input_7_0").click()
tempoEspera.sleep(2)

#Marca a cor verde
navegador.find_element(By.ID, "label_input_7_4").click()
tempoEspera.sleep(2)

#marcando a avaliaçao
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]' ).click()
tempoEspera.sleep(2)

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marca como muito satisfeito a Qualidade do Serviço
navegador.find_element(By.ID, "input_9_0_3").click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Marca como satisfeito o Grau de Dificuldade
navegador.find_element(By.ID, "input_9_1_2").click()

#Tempo para o computador abrir o formulário
tempoEspera.sleep(2)

#Enviar informações
navegador.find_element(By.ID, "input_2").click()
tempoEspera.sleep(2)


