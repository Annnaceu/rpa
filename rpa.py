from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import time
import pandas as pd

navegador = opcoesSelenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
time.sleep(5)


elementoTabela = navegador.find_element(By.XPATH,'//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

dataFrameLista = []

linha = 1
for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)

    linha = linha + 1

arquivoExcel = pd.ExcelWriter('dadosSite.xlsx' , engine='xlsxwriter')
arquivoExcel.close()


#prepara o arquivo do excel usando xlxwriter
dataFrame = pd.DataFrame(dataFrameLista, columns=['Nome-Dados'])
arquivoExcel = pd.ExcelWriter('dadosSite.xlsx' , engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Sheet1' , index=True)


arquivoExcel.close()