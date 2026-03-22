class Car:
    def __init__(self,model,colour,year):
        self.model=model
        self.colour=colour
        self.year=year

    def drive(self):
        print(f"you drive {self.model}")