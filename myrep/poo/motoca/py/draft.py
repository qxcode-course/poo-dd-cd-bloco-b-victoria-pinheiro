class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age

    def getName(self) -> str:
        return self.__name
    
    def getAge(self) -> int:
        return self.__age
    
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"

class Moto:
    def __init__(self, power: int = 1):
        self.__person: Pessoa | None = None
        self.__power: int = power
        self.__time: int = 0
    
    def getPerson(self) -> Pessoa | None:
        return self.__person
    
    def getPower(self) -> int:
        return self.__power
    
    def getTime(self) -> int:
        return self.__time
    
    def insertPerson(self, Pessoa: Pessoa) -> bool:
        if self.__person != None:
            return False
        else:
            self.__person = Pessoa
            return True

    def remove(self) -> Pessoa | None:
        if self.__person == None:
            return None
        else:
            Aux: Pessoa = self.__person
            self.__person = None
            return Aux

    def honk(self) -> str:
        honk: str = ""
        for i in range(self.__power):
            honk += "e"

        return honk
    
    def buyTime(self, time: int) -> None:
        self.__time += time

    def drive(self, time: int) -> None:
        if self.__time == 0:
            print("fail: buy time first")
        elif self.__person is None:
            print("fail: empty motorcycle")
        elif self.__person.getAge() > 10:
            print("fail: too old to drive")
        elif self.__time < time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= time

    def __str__(self) -> str:
        if self.__person is None:
            person_str = "(empty)"
        else:
            person_str = f"({self.__person})"
        return f"power:{self.__power}, time:{self.__time}, person:{person_str}"
    
def main():
    moto = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "show":
            print(moto)
        elif args[0] == "end":
            break
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa(nome, idade)
            if not moto.insertPerson(pessoa):
                print("fail: busy motorcycle")
        elif args[0] == "init":
            moto = Moto(int(args[1]))
        elif args[0] == "leave":
            pessoa = moto.remove()
            if pessoa is not None:
                print(pessoa)
            else: print("fail: empty motorcycle")
        elif args[0] == "buy":
            moto.buyTime(int(args[1]))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "honk":
            print(f"P{'e' * moto.getPower()}m")
    
main()





     