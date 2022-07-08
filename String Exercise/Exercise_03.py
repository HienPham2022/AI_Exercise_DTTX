#Nối một chuỗi mới vào vị trí giữ của chuỗi đã cho
def append_middle(s1,s2):
    print("Original string are:",s1,s2)
    mid = int(len(s1)/2)
    x = s1[:mid]
    x +=s2
    x += s1[mid:]
    print("After appending new string in middle:",x)
append_middle("phamvan","hien")

