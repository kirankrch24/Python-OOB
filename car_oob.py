class Car:
    # The constructor (initializer) method
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    # A method to accelerate the car
    def accelerate(self, amount):
        self.speed += amount
        return self.speed

    # A method to brake the car
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        return self.speed

    # A method to display the car's information
    def display_info(self):
        print(f"{self.color} {self.year} {self.make} {self.model} - Speed: {self.speed} km/h")

# Create a Car object (instance)
my_car = Car("Tesla", "Model S", 2022, "Red")
my_h_c = Car("Hyundia","i10",2016,'White')

# Accelerate the car
my_car.accelerate(50)

# Brake the car
my_car.brake(20)

# Display the car's information
my_car.display_info()
my_h_c.display_info()