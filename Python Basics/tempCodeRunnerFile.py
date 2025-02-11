#lastly, using classes and methods
class Switch:
    def num_one(self):
        return "One"
    def num_two(self):
        return "Two"
    def num_three(self):
        return "Three"
    def num_four(self):
        return "Four"
    def default(self):
        return "Unknown number"
    
    def switch(self, value):
        return {
            1: self.num_one,
            2: self.num_two,
            3: self.num_three,
            4: self.num_four,
        }.get(value, self.default) #if the user entered a number that is above 4, it will call the default function

ans = Switch()
res = ans.switch(2) 
print(res) #prints "Two"