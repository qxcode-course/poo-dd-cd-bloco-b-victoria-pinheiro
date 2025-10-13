class Chinela:
    def __init__(self):                                                                
        self.__tamanho = 0                                                                                                                                                  

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, value: int):
        if value < 20 or value > 50:
            print("fail: tamanho deve estar entre 20 e 50")
        elif value % 2 != 0:
            print("fail: tamanho tem que ser um número par")
        else:
            self.__tamanho = value

def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0:
        print("digite seu tamanho de chinela")
        tamanho = int(input())
        chinela.setTamanho(tamanho)
    print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())

main()
chinela = Chinela()
    
while chinela.getTamanho() == 0:
    print("digite seu tamanho de chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)

print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())
