#chuyển các phần từ trong list thành bình phương của nó
from cgitb import reset


numbers = [1,2,3,4,5,6]
result = []
for i in numbers:
    result.append(i*i)
print(result)