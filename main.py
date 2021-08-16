# Coding: "utf-8"

__author__ = "Bruno Sevalho Wesen"
__author2__ = "Gabriely da Mata Batista"

__version__ = "1.3"

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.utils import get_color_from_hex as ku
from kivymd.uix.label import MDLabel

# Variáveis Globais
listcard = []


class Manager(ScreenManager):
    pass


class Tela1(Screen):

    def adicionarMdCard(self):
        self.ids.caixa.add_widget(listcard[0])
        listcard.pop()


class Tela2(Screen):

    def apagarTexto(self):
        texto = self.ids.texto_anotacao
        mdcard = MDCard(size_hint=(0.6, None), height=100,
                        pos_hint={"center_x": 0.5, "center_y": 0.85})
        mdcard.md_bg_color = ku("#ebd936")
        mdcard.add_widget(MDLabel(text=texto.text, halign="center"))
        listcard.append(mdcard)
        texto.text = ""


class Tela3(Screen):
    pass


class Programa(MDApp):
    pass

if __name__ == "__main__":
    Programa().run()
