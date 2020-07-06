class Person:
    def __init__(self,name,age):
        self._name= name
        self._age= age
    @property  #属性
    def name(self):
        return self._name
    # def get_name(self):
    #     return self._name
    def rename(self,new_name):
        self._name = new_name

p = Person('wong',12)
p.name  # 不用加()
# print(p.get_name())
# print(p.rename('song lei'))
# print(p.get_name())

class Student(Person):
    def set_score(self, score):
        self._score=score

    def get_score(self):
        return self._score
s = Student('liu',24)
# print(s.get_name())
s.set_score(100)
print(s.get_score())