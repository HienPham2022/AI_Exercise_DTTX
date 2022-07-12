#cho 2 set, cập nhật set 1 với những items tồn tại duy nhất 
#ở bộ đầu tiên mà không tồn tại ở bộ thứ 2
set_01 = {1,2,3,4}
set_02 = {3,4,5,6}
set_01.difference_update(set_02)
print(set_01)
