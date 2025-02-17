from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing machine is now ON"
    
    def turn_off(self):
        return "Washing machine is now OFF"

class Refrigerator(Appliance):
    def turn_on(self):
        return "Refrigerator is now ON"
    
    def turn_off(self):
        return "Refrigerator is now OFF"

def operate_appliance(appliance):
    print(appliance.turn_on())
    print(appliance.turn_off())

def main():
    washing_machine = WashingMachine()
    refrigerator = Refrigerator()  

    operate_appliance(washing_machine)
    operate_appliance(refrigerator)

if __name__ == "__main__":
    main()