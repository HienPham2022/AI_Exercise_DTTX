#Tính tổng và tích của 2 số
def Tong_Tich(num1,num2):
    Tich=num1*num2
    if Tich <=1000:
        return Tich
    else:
        return num1+num2
Kq = Tong_Tich(10,50)
print("Kết quả là",Kq)
Kq = Tong_Tich(60,30)
print("Kết quả là:",Kq)
