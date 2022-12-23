from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cliente = ""
fila = ""
usuario = ""
senha = ""

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_experimental_option("detach", True)
chrome_driver_binary = "C:\ProgramData\chocolatey\lib\chromedriver\tools"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get('https://top.br.atos.net/')
usernameInput= driver.find_element(By.XPATH,  "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input")
PasswordInput = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td[2]/input")
ButtonInput = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/button")
usernameInput.send_keys(usuario)
PasswordInput.send_keys(senha)
ButtonInput.click()

wdw = WebDriverWait(driver, 10)
locator = (By.XPATH, "/html/body/iframe")
wdw.until(EC.presence_of_element_located(locator))
driver.get("https://top.br.atos.net/canais/sc/chamados/search_requests.cfm")


clienteInput = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[13]/td[2]/input")
grupoInput = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[29]/td[2]/input[1]")
ButtonInput = driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[53]/td[1]/button")
clienteInput.send_keys(cliente)
grupoInput.send_keys(fila)

drpStatus = Select(driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[8]/td[2]/select"))
drpStatus.select_by_visible_text("Waiting for Approval")

drpCount = Select(driver.find_element(By.XPATH, "/html/body/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[50]/td[2]/select"))
drpCount.select_by_visible_text("100")

ButtonInput.click()