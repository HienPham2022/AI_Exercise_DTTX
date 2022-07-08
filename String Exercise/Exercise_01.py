#Tạo ra 1 chuỗi được tạo thành từ kí tự đầu,giữa,và cuối cùng.
import sre_compile


str1 = "hienpham"
print("original string is: ",str1)
res = str1[0]
length = len(str1)
middle = int(length/2)
res += str1[middle]
res += str1[length-1]
print("New String is:",res)