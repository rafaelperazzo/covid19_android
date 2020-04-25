# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

html = requests.get('https://apps.yoko.pet/covid').text

soup = BeautifulSoup(html, 'html.parser')

valores = soup.find_all("div",{"class": "value"})
atualizacao = soup.find_all("a",{"class": "ui green label"})[0].get_text().rstrip()

elementos = []
for valor in valores:    
    elemento = valor.get_text().rstrip()
    elemento = elemento.lstrip()
    elementos.append(elemento)

print(elementos)
print(atualizacao)