from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.card import MDCard, MDCardSwipe
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList

Window.size = (480, 620)

class AddReceita(MDCard):
    ...

class CardReceita(MDCardSwipe):
    ...

class ReceitaInformacoes(MDScreen):
    ...

class ListaReceitas(MDList):
    def adicionar_receita(self):
        self.add_widget(CardReceita())

class TelaPrincipal(MDFloatLayout):
    def adicionar_receita(self):
        self.add_widget(AddReceita())

class AssaCuca(MDApp):
    def build(self):
        self.receita_texto = ''
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_file("main.kv")

AssaCuca().run()
