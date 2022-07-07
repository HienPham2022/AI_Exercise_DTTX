#In ra tổng từ 1 tới số nhập vào
s = 0
n = int(input('Nhập vào số cần tính tổng:'))
for i in range(1,n+1,1):
    s+= i
print("\n")
print('Tổng là:',s)