

class Car():
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0
        
    def get_descriptive_name(self):        
        return print(f"""The year of the car is {self.year}. The make of the car is {self.make}. The model of the car is {self.model}. The color of the car is {self.color}.""")
    
    def read_odometer(self):
        return print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            return print(f"Odometer updated to {self.odometer_reading} miles.")
        else:
            return print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        return print(f"Odometer incremented by {miles} miles. Total is now {self.odometer_reading} miles.")



class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def calculate_range(self):
        if self.battery_size >= 0:
            return self.battery_size * 3 + 50
        else:
            print("Battery size must be a positive integer.")

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
       
       
        
class Engine():
    def __init__(self, engine_size=2.0):
        self.engine_size = engine_size
        
    def describe_engine(self):
        print(f"This car has a {self.engine_size}-L engine.")
        
    def calculate_maximum_acceleration(self):
        if self.engine_size >= 0:
            return self.engine_size * 2 + 5
        else:
            print("Engine size must be a positive number.")
        
        
        
class ElectricCar(Car):  # 只继承Car
    def __init__(self, make, model, year, color, battery_size=75, engine_size=2.0):
        super().__init__(make, model, year, color)
        self.battery = Battery(battery_size)  # combine Battery
        self.engine = Engine(engine_size)      # combine Engine
        
    def describe_power_system(self):
        """describe dynamic system of the car"""
        self.battery.describe_battery()
        self.engine.describe_engine()
        return print(f"This car has a {self.battery.battery_size}-kWh battery and a {self.engine.engine_size}-L engine.")
    
    def get_total_range(self):
        """If the car is a hybrid, calculate total range from both battery and engine"""
        battery_range = self.battery.calculate_range()
        # Assume one liter of fuel gives 10 miles of range for simplicity
        engine_range = self.engine.engine_size * 10
        return print(f"Total hybrid range: {battery_range + engine_range} miles")

my_tesla = ElectricCar('tesla', 'model s', 2020, 'red', battery_size=100, engine_size=10)

my_tesla.get_descriptive_name()

my_tesla.increment_odometer(100)

my_tesla.describe_power_system()

my_tesla.get_total_range()

#my_tesla.read_odometer()

