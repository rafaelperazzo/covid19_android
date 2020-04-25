# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from bs4 import BeautifulSoup
import requests

def getValores():
    html = requests.get('https://apps.yoko.pet/covid').text

    soup = BeautifulSoup(html, 'html.parser')

    valores = soup.find_all("div",{"class": "value"})
    atualizacao = soup.find_all("a",{"class": "ui green label"})[0].get_text().rstrip()
    elementos = [atualizacao]
    for valor in valores:    
        elemento = valor.get_text().rstrip()
        elemento = elemento.lstrip()
        elementos.append(elemento)

    return(elementos)

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
      super(MainScreen, self).__init__(**kwargs)
      Window.clearcolor = (1, 1, 1, 1)
      self.cols = 3
      
      covid_image = Image(source="corona.jpg")
      ufca_image = Image(source="ufca.png")
      self.add_widget(covid_image)
      titulo = Label(text='MONITORAMENTO DO COVID19 NA REGIÃO DO CARIRI',color=[0,0,0,1],text_size=(250,None),bold=True,font_size='18sp',halign='center')
      self.add_widget(titulo)
      self.add_widget(ufca_image)
      
      try:
          valores = getValores()
      except requests.RequestException:
          valores = ['ERRO','0','0','0','0','0','0']
      except Exception:
          valores = ['ERRO','0','0','0','0','0','0']
      
      self.add_widget(Label(text=''))  
      self.add_widget(Label(text='Atualizado em: ' + valores[0],color=[0,0,0,1]))
      self.add_widget(Label(text=''))

      confirmados = Label(text='CONFIRMADOS',color=[0,0,0,1],bold=True)    
      self.add_widget(confirmados)
      
      analise = Label(text='EM ANÁLISE',color=[0,0,0,1],bold=True)    
      self.add_widget(analise)
      
      obitos = Label(text='ÓBITOS',color=[0,0,0,1],bold=True)    
      self.add_widget(obitos)

      valores = getValores()

      confirmados_total = Label(text=valores[1],color=[0,0,0,1],font_size='38sp',halign='center')    
      self.add_widget(confirmados_total)
      
      analise_total = Label(text=valores[2],color=[0,0,0,1],font_size='38sp',halign='center')    
      self.add_widget(analise_total)
      
      obitos_total = Label(text=valores[3],color=[0,0,0,1],font_size='38sp',halign='center')    
      self.add_widget(obitos_total)
      
      exames = Label(text='EXAMES REALIZADOS',color=[0,0,0,1],bold=True)
      self.add_widget(exames)
      
      negativos = Label(text='NEGATIVOS',color=[0,0,0,1],bold=True)    
      self.add_widget(negativos)
      
      por100mil = Label(text='POR CEM MIL',color=[0,0,0,1],bold=True)
      self.add_widget(por100mil)

      exames_total = Label(text=valores[4],color=[0,0,0,1],font_size='38sp',halign='center')
      self.add_widget(exames_total)
      
      negativos_total = Label(text=valores[5],color=[0,0,0,1],font_size='38sp',halign='center')    
      self.add_widget(negativos_total)
      
      por100mil_total = Label(text=valores[6],color=[0,0,0,1],font_size='38sp',halign='center')
      self.add_widget(por100mil_total)
      
class CovidApp(App):

    def build(self):
        return (MainScreen())


if __name__ == '__main__':
    CovidApp().run()