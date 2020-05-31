#encoding:utf-8
import models as mod
from models.Risco import Risco
from models.Protecao import TipoProtecao
from models.EPI import EPI
from models.Lab import Lab
from gui import window

'''
    Riscos
'''
# Físicos
ruido = Risco("Ruído", "FIS", 2, 5)
radiacao = Risco("Radiação", "FIS", 2, 1) 
# Quimicos
poeiras = Risco("Poeira", "QUI", 2, 2)
quims = Risco("Produtos Químicos", "QUI",4, 1)

# Biológicos
virus = Risco("Virus", "BIO", 5, 5)

# Ergonômicos
monotonia = Risco("Monotonia e repetitividade","ERG", 1, 5)

'''
    Protecoes
'''
mascara = TipoProtecao("Máscara","Protege contra diversos tipos de partículas",[virus, poeiras])

oculos = TipoProtecao(
        "Óculos", 
        "Protege contra diversos tipos de radiacao ou particulas",
        [virus, radiacao])

avental = TipoProtecao(
        "Aventais", 
        "Protege contra diversos tipos de partículas",
        [virus, poeiras, quims]) 
luvas = TipoProtecao(
        "Luvas", 
        "Protege contra diversos tipos de partículas",
        [virus, quims])

fones = TipoProtecao(
        "fones", 
        "Protege contra diversos tipos de partículas",
        [ruido])
'''
    EPIS
'''
oculos_lab = EPI("Óculos Lab", oculos, "modelo")
avental_branco = EPI("Avental", avental, "modelo")
mascara_n95 = EPI("mascara_n95", mascara, "modelo")
luvas_nitrilicas = EPI("Luvas Nitrílicas", luvas, "modelo")

'''
    Lab
'''
lab = Lab("LAB N2", "Laboratório NB2 para COVID", {virus, ruido}, {oculos, avental, luvas, fones})


def criar_lab():
    lab1 = Lab("Laboratório de extração",
               "Laboratório para extração de RNA",
               None,
            set([oculos_lab]))

    dados = [lab1, lab]
    window_ = window.GUI([Lab("Laboratório Padrão", "Laboratório padrão -  cadastre seus laboratórios")])

criar_lab()
