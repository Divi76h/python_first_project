class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def catProperty(self):
        print("This method belongs to cat only")


def Main():
    thePet = Pet("Cat", 1)

    jess = Cat("Jess", 3)

    print("Is jess a cat? " + str(isinstance(jess, Cat)))
    print("Is jess is a pet?" + str(isinstance(jess, Pet)))


if __name__ == "__main__":
    Main()
