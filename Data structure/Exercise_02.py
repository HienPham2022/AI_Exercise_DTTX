#Xóa và thêm mục vào danh sách
sample_list = [34,54,67,89,11,43,94]
print("Original list:",sample_list)
element = sample_list.pop(4)
print("list after removing element at index 4:",sample_list)
sample_list.insert(2,element)
print("list after adding element at index 2:",sample_list)
sample_list.append(element)
print("List after adding element at last :",sample_list)
