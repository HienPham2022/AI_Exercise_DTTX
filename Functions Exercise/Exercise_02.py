#Tạo 1 hàm với chiều dài(số lượng) tham số thay đổi
def func1(*agr):
    for i in agr:
        print(i)
func1(20,40,60)
func1(50,80)
