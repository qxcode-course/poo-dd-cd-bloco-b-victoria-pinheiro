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
    def __init__(self, power=1):
        self.__person = None
        self.__power = power
        self.__time = 0
    
    def getPerson(self) -> Pessoa | None:
        return self.__person
    
    def getPower(self) -> int:
        return self.__power
    
    def getTime(self) -> int:
        return self.__time
    
    def insertPerson(self, Pessoa: Pessoa) -> bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        else:
            self.__person = Pessoa
            return True

    def remove(self) -> Pessoa | None:
        if self.__person == None:
            print("fail: empty motorcycle")
            return None
        else:
            Aux: Pessoa = self.__person
            self.__person = None
            return Aux

    def honk(self) -> str:
        return "P" + "e" * self.__power + "m"
    
    def buyTime(self, time: int) -> None:
        self.__time += time

    def drive(self, time: int) -> None:
        if self.__time == 0:
            print("fail: buy time first")
            return
        elif self.__person is None:
            print("fail: empty motorcycle")
            return
        elif self.__person.getAge() > 10:
            print("fail: too old to drive")
            return
        if time > self.__time:
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
            name = args[1]
            age = int(args[2])
            moto.insertPerson(Pessoa(name, age))
        elif args[0] == "leave":
            person = moto.remove()
            if person is not None:
                print(person)
        elif args[0] == "buy":
            time = int(args[1])
            moto.buyTime(time)
        elif args[0] == "drive":
            time = int(args[1])
            moto.drive(time)
        elif args[0] == "honk":
            print(moto.honk())
        elif args[0] == "init":
            power = int(args[1])
            moto = Moto(power)

main()



     