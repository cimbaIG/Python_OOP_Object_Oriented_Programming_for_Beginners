# Example of aggregation in Python 
class Vehicle:
    
    def __init__(self, color, license_plate, is_electric):
        self.color = color
        self.license_plate = license_plate 
        self.is_electric = is_electric
        
    def show_license_plate(self):
        print(self.license_plate)
        
    def show_info(self):
        print("My vehicle:")
        print(f"Color: {self.color}")
        print(f"License plate: {self.license_plate}")
        print(f"Electric: {self.is_electric}")
        

class Employee:
    
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
                
    def show_vehicle_info(self):
        self.vehicle.show_info()
        

# Create vehicle instance
black_vehicle = Vehicle("black", "AXY 245", is_electric=False)
# Create employee instance and passing vehicle instance as attribute
employee = Employee("Gino", black_vehicle)

print(employee)
print(employee.vehicle)

employee.show_vehicle_info()

print(employee.vehicle.color)
print(employee.vehicle.license_plate)
print(employee.vehicle.is_electric)

employee.vehicle.show_license_plate()
