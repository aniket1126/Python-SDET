class book:
    def __init__(self,bname,author):
        self.bname=bname
        self.author=author

    def __str__(self):
        return f"books name :-{self.bname},author {self.author}"

obj1=book("the invisible man", 'y-colsen')
print(obj1)
