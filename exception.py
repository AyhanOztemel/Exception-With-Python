
class Exception:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Calculate():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        if self.x<10:
            return Exception("error:x cannot be < 10")
        else:
            return self.x+self.y
# example-1
print(Exception("error:Something went wrong"))  # output: "Something went wrong" 

# example-2
error=Exception("error:Something went wrong")   # output: "Something went wrong"
print(error)
        
# example-3       
calculate=Calculate(5,15)   
print(calculate.add())      # output: "x cannot be < 10"

#example-4   
calculate=Calculate(15,15)
print(calculate.add()) # output: 30
    
