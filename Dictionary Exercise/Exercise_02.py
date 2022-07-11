#hợp nhất 2 dictionary thành 1
dict_01 = {'ten':10,'twenty':20,'thirty':30}
dict_02 = {'thirty':30,'fourty':40,'fifty':50}
dict_03 = dict_01.copy()
dict_03.update(dict_02)
print(dict_03)
