class EvenNumber:
    def __init__(self, limit):
        self.limit=limit
        self.n=2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n>self.limit:
            raise StopIteration
        
        x=self.n
        self.n+=2
        return x
    
#create an iterator for even numbers upto 20
even=EvenNumber(20)

for num in even:
    print(num)