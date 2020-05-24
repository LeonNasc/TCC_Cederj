#encoding:utf-8
from . import identificavel as identificavel
class Risco(identificavel.identificavel):

    def __init__(self, nome, classificao, dano, recorrencia):
        super().__init__(nome,nome)
        self.__classificao = classificao
        self.__dano = dano
        self.__recorrencia = recorrencia
        print("Sou um risco")

    '''
        Retorna a classificação de risco legal
    '''
    def get_classificao(self):
        return self.__classificao

    ''' 
        Calcula o fator de dano do risco como produto do dano do risco e sua chance de acontecer
    '''
    def calcular_fator(self):
        return self.__dano * self__recorrencia


    def __repr__(self):
        return self.__nome
