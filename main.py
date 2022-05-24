from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import pandas as pd

class APP(BoxLayout):

    def __init__(self, **kwargs):
        super(APP, self).__init__(**kwargs)
        mybutton = Button(text = 'Afficher les informations', size_hint = (0.10,0.10), background_color = (1.0, 0.0, 0.0, 1.0))
        mybutton.bind(on_press = self.bourse)
        self.add_widget(mybutton)

    def bourse(self, bouton):
        req = requests.get('http://api.worldbank.org/v2/countries?incomeLevel=LMC&format=json')
        wb = req.json()
        wb = pd.json_normalize(wb[1])
        wb2 = pd.json_normalize(requests.get("http://api.worldbank.org/v2/countries?incomeLevel=LMC&format=json&page=2").json()[1])
        test = pd.concat([wb, wb2])
        print(wb.head(50))
        return None
    
class Application(App):
    def build(self):
        return APP()

if __name__ == '__main__':
    
    Application().run()