#Đến tần suất xuất hiên của mỗi phần tử
sample_list = [11,22,11,5,6,8,5,14,13,22,9]
print("Original list:",sample_list)
count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] +=1
    else:
        count_dict[item] =1
print("Printing count of each item:",count_dict)
