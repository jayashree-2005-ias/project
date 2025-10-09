# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

# Derived from Vehicle
class Car(Vehicle):
    def play_music(self):
        print(f"{self.brand} {self.model} is playing music ")

# Derived from Car
class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} is charging ")

# Independent class
class SmartDevice:
    def connect_wifi(self):
        print("Smart device connected to WiFi ")

# Multiple inheritance from Car and SmartDevice
class SmartCar(Car, SmartDevice):
    def auto_drive(self):
        print(f"{self.brand} {self.model} is driving autonomously ")

# Multiple inheritance from SmartCar and ElectricCar
class ElectricSmartCar(SmartCar, ElectricCar):
    def autopilot_mode(self):
        print(f"{self.brand} {self.model} is now in autopilot mode ")


# --- Object creation and method calls ---
esc = ElectricSmartCar("Toyoto", "Model S")

esc.start()           # From Vehicle
esc.play_music()      # From Car
esc.connect_wifi()    # From SmartDevice
esc.charge()          # From ElectricCar
esc.autopilot_mode()  # Own method