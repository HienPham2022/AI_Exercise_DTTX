#tạo một mảng số nguyên 5x2 từ khoảng 100 tới 200 sao cho sự khác biệt giữa mỗi phần tử là 10
import numpy

print("Creating 5X2 array using numpy.arange")
sampleArray = numpy.arange(100, 200, 10)
sampleArray = sampleArray.reshape(5,2)
print (sampleArray)