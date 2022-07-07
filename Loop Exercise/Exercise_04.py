#Đếm tổng chữ số của một số
num = 123456
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print('tổng chữ số của số đã cho là:',count)
