class Inset:
    def __init__(self):
        self.list1 = []
    
    def insert(self, element):
        if element not in self.list1:
            self.list1.append(element)
    
    def member(self, element):
        return element in self.list1

    def remove(self, element):
        if element in self.list1:
            self.list1.remove(element)
        else:
            raise ValueError("Couldn't find the element")

    def __str__(self):
        sorted_list = sorted(self.list1)
        return " ".join(map(str, sorted_list))

def main():
    my_inset = Inset()
    my_inset.insert(5)
    my_inset.insert(3)
    my_inset.insert(5)
    my_inset.insert(1)

    print("After insertions:", my_inset)

    print("Is 3 a member?", my_inset.member(3))
    print("Is 8 a member?", my_inset.member(8))

    my_inset.remove(3)
    print("After removing:", my_inset)

    try:
        my_inset.remove(10)
    except ValueError as e:
        print(e)
    


if __name__ == "__main__":
    main()