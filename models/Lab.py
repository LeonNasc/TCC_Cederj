#encoding:utf-8
from . import identificavel
class Lab(identificavel.identificavel):

    def __init__(self, nome, descricao, riscos=set(), EPI=set()):
        super().__init__(nome,descricao)
        self.__nome = nome
        self.__descricao = descricao
        self.__riscos = riscos
        self.__epis = EPI
        print("Lab iniciado")

    '''
        Método utilizado quando um usuário adicionar um EPI requerido no lab
        Atende ao caso de uso XPTO
    '''
    def incluir_EPI(self, EPI):
        self.__epis.add(EPI)
        self.validar_lab()
        pass

    '''
        Método utilizado quando um usuário remover um EPI requerido no lab
        Atende ao caso de uso XPTO
    '''
    def remover_EPI(self, EPI):
        self.__epis.remove(EPI)
        self.validar_lab()
        pass

    def adicionar_risco(self, risco):
        self.__riscos.add(risco)
        self.validar_lab()
        pass

    def remover_risco(self, risco):
        self.__riscos.remove(risco)
        self.validar_lab()
        pass

    def get_epis(self):
        return self.__epis.copy()

    '''
        Método utilizado quando um usuário registra uma leitura de EPIs
        Atende ao caso de uso XPTO
    '''
    def registrar_entrada(self):
        leitura = Leitura(self.__epis)
        leitura.avaliar() #Mudança da máquina de estados da avaliação
        estado_final = validar_riscos(leitura)
        gui.exibir_resultado(estado)
        return registro.__repr__() 

    '''
        Método para avaliar se o usuário da leitura está adequadamente protegido
    '''
    def validar_riscos(self, leitura):
        riscos = self.listar_riscos()
        protecoes = [protecao.tipo for protecao in leitura.listar_protecoes()]

    '''
        Método para avaliar se todos os riscos do lab estão protegidos por um EPI requerido
    '''
    def validar_lab(self):
        print("lab ok")
        pass
