#encoding:utf-8
from . import identificavel
class EPI(identificavel.identificavel):

    def __init__(self, nome, tipo, modelo):
        self.__nome = nome
        self.__tipo = tipo
        self.__modelo = modelo
        super()
        print("Modelo do EPI - %s carregado!"% nome)

    def atualizar_modelo(self, modelo):
        pass

    def get_modelo(self):
        return self.__modelo.get_modelo()

    def get_tipo(self):
        return self.__tipo

    def __repr__(self):
        modelo_versao = self.__modelo.get_versao()
        return "Tipo: %s\nNome: %s\nVersão: %s" % (self.__tipo, self.__nome, modelo_versao)
