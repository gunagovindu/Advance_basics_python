class student:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def get_name(self):
        print(f"the student name is{self._name}")
    def get_age(self):
        print(f" the age is {self._age}")

    def set_age(self,new_age):
        if new_age>5:
            self._age=new_age
s1=student("guna",24)
s1.get_name()
s1.get_age()
s1.set_age(30)
s1.get_age