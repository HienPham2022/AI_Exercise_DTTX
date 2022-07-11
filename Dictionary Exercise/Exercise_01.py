#chuyển 2 list thành dictionary
keys = ['ten','twenty','thirty']
values = [10,20,30]
res_dic = dict()
for i in range(len(keys)):
    res_dic.update({keys[i]:values[i]})
print(res_dic)
