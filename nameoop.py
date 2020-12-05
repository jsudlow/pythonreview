class Name:
    count=0
    first=""
    last=""
    middle=""
    suffix=""


    def __init__(self, name=""):
        x = name.split(" ")
        self.count = len(x)
        #print(self.count)
        if self.count == 4:
            self.first = x[0]
            self.middle = x[1]
            self.last = x[2]
            self.suffix = x[3]
        elif self.count == 3:
            self.first = x[0]
            self.middle = x[1]
            self.last = x[2]
        elif self.count == 2:
            self.first = x[0]
            self.middle = x[1]
        elif self.count == 1:
            self.first = x[0]
    def set_first(self,value):
        if self.get_first() and value == "":
            self.count -=1
        if self.get_first() =="" and value !="":
            self.count += 1
        self.first = value
    def set_middle(self,value):
        if self.get_middle() and value == "":
            self.count -=1
        if self.get_middle() =="" and value !="":
            self.count += 1
        self.middle = value
       
    def set_last(self,value):
        if self.get_last() and value == "":
            self.count -=1
        if self.get_last() =="" and value !="":
            self.count += 1
        self.last = value
      
    def set_suffix(self,value):
        if self.get_suffix() and value == "":
            self.count -=1
        if self.get_suffix() =="" and value !="":
            self.count += 1
        self.suffix = value
       
    def get_first(self):
        return self.first
    def get_middle(self):
        return self.middle
    def get_last(self):
        return self.last
    def get_suffix(self):
        return self.suffix
    def get_count(self):
        return self.count
    def get_name(self):
        name=""
        if self.first != "":
            name += self.first + " "
        if self.middle != "":
            name +=self.middle + " "
        if self.last != "":
            name += self.last + " "
        if self.suffix != "":
            name += self.suffix
        return name
    def get_initials(self):
        initials = ""
        if self.first != "":
            initials += self.first[0]
        if self.middle != "":
            initials += self.middle[0]
        if self.last != "":
            initials += self.last[0]
        return initials
name_null = Name("")
print(name_null.get_name())
name_null.set_last("Williamson")
print(name_null.get_name())
name = Name("Robert John")
print(name.get_name())
#print('\n')

name.set_last("Downy")
print(name.get_name())
#print('\n')
name.set_suffix("Jr")
print(name.get_name())
name.set_last("")
print(name.get_name())