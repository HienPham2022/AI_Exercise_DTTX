#Tạo 1 chuỗi mới được tạo thành từ kí tự đầu,giữa và cuối của mỗi chuỗi input
def mix_string(s1,s2):
    frist_char = s1[0]+s2[0]
    mid_char = s1[int(len(s1)/2)]+s2[int(len(s2)/2)]
    last_char = s1[len(s1)-1]+s2[len(s2)-1]
    result = frist_char + mid_char + last_char
    print("Mix string is: ",result)
s1 = "abcdef"
s2 = "123456"
mix_string(s1,s2)
