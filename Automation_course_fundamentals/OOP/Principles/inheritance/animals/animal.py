class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        Print a greeting message for the animal.
        """
        print(f"{self.name} says hi!")


