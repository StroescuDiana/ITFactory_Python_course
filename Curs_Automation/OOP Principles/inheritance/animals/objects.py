from inheritance.animals.animal import Animal
from inheritance.animals.dog import Dog

# Create an instance of the Animal class
animal = Animal("Generic animal")
animal.speak()

# Create an instance of the Dog subclass
dog = Dog("Fido", "Golden Retriever")
dog.speak()
print(dog.breed)

