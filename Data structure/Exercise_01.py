#tạo một danh sách được tạo thành từ những 
# chỉ mục lẻ của những items từ danh sách thứ 1 và chẵn từ danh sách thứ 2
list1 = [3,6,9,12,15,18,21]
lits2 = [4,8,12,16,20,24,28]
odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)
even_elements = lits2[0::2]
print("Element at even-index position from list two")
print(even_elements)