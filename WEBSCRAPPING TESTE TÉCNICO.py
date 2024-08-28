from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

serviceContact = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=serviceContact)

listLinksWithDeadpool = []
listTitlesAndDates = []

#nav.get('https://www.omelete.com.br/')  LINK PARA TESTAR O CÓDIGO TAMBÉM

nav.get('https://www.omelete.com.br/busca?q=DEADPOOL')

links = nav.find_elements(By.TAG_NAME,'a')
urls = [link.get_attribute('href') for link in links]

pattern = re.compile(r'deadpool', re.IGNORECASE)

for url in urls:
    if url and pattern.search(url):
        listLinksWithDeadpool.append(url)

for link in listLinksWithDeadpool:
    nav.get(link)

    try:
        title = nav.find_element(By.XPATH, '/html/body/main/div[1]/section/div[1]/div/div/article/div[2]/div/div[2]/h1').text
        date = nav.find_element(By.XPATH, '/html/body/main/div[1]/section/div[1]/div/div/article/div[2]/div/div[5]/div/div[2]/div[1]').text

        listTitlesAndDates.append({'title': title, 'date': date})
    except Exception as e:
        print(f"Erro ao extrair dados do link: {link}: {e}")

nav.quit()

with open('resultados.txt', 'w', encoding='utf-8') as file:
    for results in listTitlesAndDates:
        file.write(f"{results['title']}\n")
        file.write(f"{results['date']}\n")
        file.write("_____________________\n")

print('Os títulos e datas das publicações estão salvos no arquivo: "resultados.txt".')



