from inheritance.animals.animal import Animal


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        """
        Print a barking message for the dog.
        """
        print(f"{self.name} barks!")
