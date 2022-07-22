# Tạo 1 lớp con tên Bus, lớp này sẽ kế thừa những biến và
#phương thức của lớp vehicle
class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo",180,12)
print("Vehicle Name:",School_bus.name,"Speed:",School_bus.max_speed,"Mileage:",School_bus.mileage)

