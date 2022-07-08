#Tạo một chuỗi được hình thành từ 3 ký tự giữa của chuỗi
def get_middle_three_chars(str1):
    print("Original String is:",str1)
    mid = int(len(str1)/2)
    res = str1[mid -1 :mid +2]
    print("Middle three chars are:",res)
get_middle_three_chars("phamvanhien")
get_middle_three_chars("hienpham")