#Sau đây là mảng numPy được cung cấp. Trả về mảng các mục bằng cách lấy cột thứ ba từ tất cả các hàng
import numpy

sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
print("Printing Input Array")
print(sampleArray)

print("\n Printing array of items in the third column from all rows")
newArray = sampleArray[...,2]
print(newArray)