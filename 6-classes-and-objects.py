# Yeah, I know. What I'm doing is super basic. I haven't coded in years, since I've been working
# as an IT Technician / IT Support / System Administrator. I'm doing this for practice.

# we use classes and objects for re-usability
# init function is called whenever an instance of the class Dog is created
# self is a variable
# good practice to use capital letter in the beginning of Class name,
# and use lower case in variable names

class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + " says: Bark!")

# giving the dog a name
my_dog = Dog("Askal")
another_dog = Dog("Browny")

# another example of using the class
# run the code to see the result
my_dog.speak()

# another instance
another_dog.speak()