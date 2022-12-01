#aqui ta os imports das bibliotecas

from selenium import webdriver
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys

#navegação ate o wpp web

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

#definir contatos e grupos + mensagem 

contacts = [''] #contato ou grupo conforme está salvo no aparelho 
message = '' #mensagem a ser enviada

#busca por contato/grupo

def search_contact(contact):
    field_search = driver.find_element("xpath",'//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(5)
    field_search.click()
    field_search.send_keys(contact)
    time.sleep(5)
    field_search.send_keys(Keys.ENTER)

def send_message(message):
    field_message = driver.find_element("xpath",'//div[contains(@class,"fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv")]')
    field_message.click()
    time.sleep(5)
    field_message.send_keys(message)
    time.sleep(5)
    field_message.send_keys(Keys.ENTER)

for contact in contacts:
    search_contact(contact)
    time.sleep(5)
    send_message(message)