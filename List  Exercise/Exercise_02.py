#Nối 2 chuỗi thông qua chỉ số index,sử dụng hàm zip()
list1 = ['m','na','i','hien']
list2 = ['y','me','s','pham']
list3 = [i+j for i,j in zip(list1,list2)]
print(list3)