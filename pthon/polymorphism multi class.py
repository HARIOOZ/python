class dog:
    def sound(self):
        print("barks")
class cat:
    def sound(self):
        print("meow")
class sheep:
    def sound(self):
        print("mehhh") 
def make_sound(animal):
    animal.sound()      
dogs=dog()
cats=cat()
sheeps=sheep()

make_sound(dogs)
make_sound(cats)
make_sound(sheeps)
