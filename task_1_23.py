class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, v):
        self._name = v

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, v):
        if v < 0:
            raise ValueError("Age cannot be negative.")
        self._age = v

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}" 

    def __str__(self):
        return self.get_info()

def main():
    p1 = Person("Shako", 17)
    p2 = Person("Nino", 38)

    print(p1.get_info())
    print(p2.get_info())
    
    try:
        p1.age = -19
    except Exception as ex:
        print("Error:", ex)


if __name__ == "__main__":
    main()