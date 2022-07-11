#Nói 2 list theo thứ tự
list_1 = ["Hello ","take "]
list_2 = ["Dear","Sir"]
result = [ x +y for x in list_1 for y in list_2]
print(result)