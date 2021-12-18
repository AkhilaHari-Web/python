class Student:
    name = 'Arjun'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    @classmethod
    def class_info(cls):
        return cls.name
    @staticmethod
    def static_avg():
        return (a + b) / 2

    
a=int(input("first subject Marks::"))
b=int(input("secound subject Marks::"))
s1 = Student(a,b)
print(s1.class_info())
print(Student.static_avg())


