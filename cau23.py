s = input("Nhập câu của bạn: ")
d={"số":0, "chữ":0}
for c in s:
 if c.isdigit():
    d["số"]+=1
 elif c.isalpha():
        d["chữ"]+=1
 else:
     pass
print ("Số chữ cái là:", d["chữ"])
print ("Số chữ số là:", d["số"])
