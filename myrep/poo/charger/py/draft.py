class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCapacidade(self) -> int:
        return self.__capacidade
    
    def getCarga(self) -> int:
        return self.__carga
    
    def consumir(self, minutos: int) -> int:
        usado = min(minutos, self.__carga)
        self.__carga -= usado
        return usado
    
    def carregar(self, minutos: int, potencia: int) -> None:
        self.__carga = min(self.__capacidade, self.__carga + minutos * potencia)

    def adicionarCarga(self, quantidade: int) -> None:
        self.__carga = min(self.__capacidade, self.__carga + quantidade)

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

    def getPotencia(self) -> int:
        return self.__potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria = None
        self.__carregador = None
        self.__tempoLigado: int = 0
            
    def setBateria(self, capacidade: int) -> None:
        self.__bateria = Bateria(capacidade)

def main():
    notebook = Notebook()
    while True:
        
main()
