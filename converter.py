class convertor:
    def __init__(self,n,name):
        self.value=n
        self.name=name
    def feetintoinches(self):
        inches=self.value*12
        print(inches)
    def feettomiles(self):
        miles=self.value*0.00018939
        print(miles)
    def feettoyards(self):
        yards=self.value*0.3333
        print(yards)
    def milestokm(self):
        km=self.value/0.62137
        print(km)
n=float(input('enter feet/inches/cm/mm/km'))
x=convertor(n,'inches')
x.feettomiles()
x.feettoyards()
        