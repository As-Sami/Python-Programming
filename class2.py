class person:
    name = ''
    age = 0
    gender = None
    def __init__(self, name , age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def output(self):
        print('Name:',self.name)
        print('Age: ',self.age)
        print('Gender:',self.gender)

class coder(person):
    skills = None
    def add_skill(self, skill):
        if(self.skills==None):
            self.skills = [skill]
        else:
            self.skills.append(skill)

    def output_all(self):
        self.output()
        print('Skill:',self.skills)
        print('--------------------------')

p1 = person('Shishir',20,'Male')
p2 = person('Oli',22,'Male')
p3 = person('Bijoy',21,'Male')

p1.output()
print('-----------')
p2.output()
print('-----------')
p3.output()
print('-----------')

p4 = coder('Nihan', 21 , 'Male')
p5 = coder('Alomgir', 21 , 'Male')

p4.add_skill('Implementation')
p5.add_skill('Graph')
p5.add_skill('Segmented Tree')

p4.output()
print('')
p4.output_all()
p5.output()
print('')
p5.output_all()
