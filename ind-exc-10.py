# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    # your code goes here


car1 = Vehicle()
car2 = Vehicle()
# test code
print(car1.description("Fer", "Red", "Convertible" "$60,000.00"))
print(car2.description("Jump", "Blue", "Van", "$10,000.00"))
