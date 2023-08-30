'''

  - create student: name --> welcome
  -add mark
  -get avg






'''
class student:
    def name(self ,name):
        print(f"welcome {name}")
        self.marks=[]

    def addmark(self,mark):
        self.marks.append(mark)
        print(self.marks)

    def avg(self):
        arge =sum(self.marks) / len(self.marks)
        print(arge)







c=student()
c.name("omar")
c.addmark(31)
c.addmark(51)
c.addmark(41)
c.addmark(71) 
c.avg()

c1=student()
c1.name("moooo")
c1.addmark(31)
c1.addmark(881)
c1.addmark(891)
c1.addmark(721) 
c1.avg()

c10=student()
c10.name("mortrooo")
c10.addmark(31)
c10.addmark(71)
c10.addmark(91)
c10.addmark(21) 
c10.avg()
