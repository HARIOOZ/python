class car:
    def __init__(self,make,model,year):
        self.__make=make
        self.__model=model
        self.__year=year
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year

    def set_make(self,make):
        self.__make=make
    def set_model(self,model):
        self.__model=model
    def set_year(self,year):
        self.__year=year
        if year<=2024:
            self.__year=year
        else:
            print("given year is invalid")
car1=car("toyota","corolla",2020)
print(f"car make:{car1.get_make()}\ncar year:{car1.get_year()}")

car1.set_make("volkswagen")
car1.set_model("polo")
car1.set_year(2023)
print(f"new car make:{car1.get_make()}\nnew car model:{car1.get_model()}\nnew car year:{car1.get_year()}")