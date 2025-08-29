class MyClass:

    def __init__(self,number):
        self.number = number

    def round_number(self):
        return round(self.number)

    def add_to_rounded_number(self,number_to_add):
        return self.round_number()+number_to_add

my_instance = MyClass(number = 5.2)
my_sum = my_instance.add_to_rounded_number(number_to_add = 3)
print(my_sum)
        