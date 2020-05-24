#encoding:utf-8
class identificavel:

    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao


    def get_ID(self):
        return self.__hash__()
