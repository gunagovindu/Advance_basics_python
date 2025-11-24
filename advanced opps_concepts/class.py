class student:
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
    

    def show_info(self):
           print(f"the student name {self.name} {self.age} years old and location {self.adress}")

class car:
     def __init__(self,brand,color,engine):
          self.color=color
          self.brand=brand
          self.engine=engine
     def info(self):
          print(f"the color is {self.color} show room {self.brand} and power is {self.engine} cc")


s1=student("guna",24,"kvp")
s2=student("dhanu",25,"rct")

s1.show_info()
s2.show_info()

c1=car("grey","thar",200)
c2=car("white","mahindra",300)

c1.info()
c2.info()