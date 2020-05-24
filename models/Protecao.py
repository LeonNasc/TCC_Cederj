#encoding:utf-8
from . import identificavel
class TipoProtecao(identificavel.identificavel):

    def __init__(self, nome, descricao, riscos):
        self.__nome = nome
        self.__descricao = descricao
        self.__riscos = riscos
        print("Eu protego contra %s" % self.get_protecoes())

    def get_protecoes(self):
        return [risco.get_nome() for risco in self.__riscos]
