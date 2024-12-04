
class Library:
    totalbooks = 0
    def newbooks(self,new):
        self.totalbooks += new
        print(self.totalbooks)
mc=Library()

mc.newbooks(5)
mc.newbooks(10)



