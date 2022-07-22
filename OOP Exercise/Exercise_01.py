# tạo 1 lớp với các thuộc tính đối tượng
#viết chương trình tạo 1 lớp vehicle với max_speed
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed

        self.mileage = mileage
    
modelX = Vehicle(240,18)
print(modelX.max_speed,modelX.mileage)
