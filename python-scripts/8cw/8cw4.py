class tomato:
    def __init__(self, index):
        self.index=index
        self.stages = {0:'netu', 1:'cvetet', 2:'zeleniy', 3:'krasniy'}

    def func(abc):
        abc.index +=1
        return abc.index
    def getstag(abc):
        if abc.index ==0:
            return abc.stages[0]
    def getstage(abc):
        if abc.index ==1:
            abc.stage == 1
    def getsta(abc):
        if abc.index ==2:
            abc.stage == 2
    def getst(abc):
        if abc.index ==3:
            abc.stage == 3
x = tomato(0)

print(x.getstag())
print(x.getstage())
print(x.getsta())
print(x.getst())