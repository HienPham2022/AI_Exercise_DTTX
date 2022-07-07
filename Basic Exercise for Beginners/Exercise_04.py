#Xóa n ký tự đầu tiên từ chuỗi
def Xoa_Char(chuoi,n):
    print('Chuỗi ban đầu:', chuoi)
    x = chuoi[n:]
    return x
print('Xóa ký tự từ chuỗi')
print(Xoa_Char("phamvan",4))
print(Xoa_Char("phamvan",2))