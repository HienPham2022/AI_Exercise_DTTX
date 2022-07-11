#khởi tạo một dict với giá trị mặc định
employees = ['kelly','emma']
defaults = {"designations":'developer',"salary":8000}
res = dict.fromkeys(employees,defaults)
print(res)
print(res["kelly"])