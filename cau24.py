s = str(input('Nhập tên: '))
def show(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
    print("Given string:", s)
    print("Số chữ viết hoa:", count_upper)
    print("Số chữ viết thường:", count_lower)
show(s)
