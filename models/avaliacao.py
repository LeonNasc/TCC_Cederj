#encoding:utf-8
import datetime
class Avaliacao:

    self._TEMPORIZADOR = 30

    def __init__(self, epis, camera):
        self.__data = datetime.datetime.now()
        self.__estado = 0 #Estado inicial da máquina de estados
        self.__epis = epis
        self.__correto = False #Estado inicial da máquina
        self.__camera = camera
        pass

    def avaliar(self):
        feed = self.obter_feed(camera)
        for frame in feed:
            estado = detectar_epis(frame)

        #Se todos os epis estão presentes, o usuário está correto
        self.__correto = estado == len(epis)
        salvar_avaliacao()

    def salvar_avaliacao(self):
        return (str(self.__data),self.__estado,self.__correto)

    def detectar_epis(self, frame):
        # Normalizar frame
        # Setar estado para 0
        # Para cada modelo de EPI, verificar presença
        # Mudar estado para cada EPI detectado
        # retornar estado do frame
        pass
        
        


   
