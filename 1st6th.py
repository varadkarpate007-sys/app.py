class Car:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)

    def refuel(self):
        print("Refueling the car with", self.fuel_type)


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        # Reusing the constructor of Car using super()
        super().__init__(brand, model, "Electric")

        self.battery_capacity = battery_capacity

    def refuel(self):
        print("Charging the electric car battery")

    def display_info(self):
        super().display_info()
        print("Battery Capacity:", self.battery_capacity, "kWh")


# Creating objects
car1 = Car("Toyota", "Fortuner", "Petrol")

electric_car1 = ElectricCar("Tesla", "Model S", 100)


# Normal Car
print("Normal Car:")
car1.display_info()
car1.refuel()

print()

# Electric Car
print("Electric Car:")
electric_car1.display_info()
electric_car1.refuel()