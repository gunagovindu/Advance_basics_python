class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("the animal sound:","woof woof")

class dog (Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

    def speak(self):
        print("the animal  is:","bark")
    def show_info(self):
        print(f"the animal name is {self.name} and the breed {self.breed}")

d1=dog("rocky","pitbull")
d2=dog("bittu","coolie")

d1.show_info()
d1.sound()

d2.show_info()
d2.speak()


