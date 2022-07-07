#In ký tự từ một chuỗi có chỉ số trong chuỗi là chẵn
chuoi = input('Nhập vào chuỗi của bạn: ')
print('chuỗi của bạn là:',chuoi)
size = len(chuoi)
print('đây là những ký tự có chỉ số chẵn:')
for i in range(0,size - 1,2):
    print("chỉ số [", i ,"]", chuoi[i])
