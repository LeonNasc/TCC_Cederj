#encoding:utf-8
import os
class Modelo:

    def __init__(self, nome, modelo_path, versao = 1):
        self.__nome = nome
        self.versao = versao
        self.modelo = self.carregar_modelo(modelo_path)
        print("Modelo %s v.%d inicializado" % (nome, versao))

    def carregar_modelo(self, path):
        #TODO código para treinar modelo conforme modelo pré-treinado
        pass

    def get_modelo(self):
        return self.modelo

    def get_versao(self):
        return self.versao

    def __repr__(self):
        return "Modelo %s v.%d" % (nome, versao)
