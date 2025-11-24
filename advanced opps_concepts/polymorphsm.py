class dog:
    def sound(self):
        return "bark"
    
class cat:
    def sound(self):
        return "meow"
class horse:
    def sound(self):
        return"Neighhhh"
    
for animal in(cat(),dog(),horse()):
    print(animal.sound())