value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
 intp = int(p, 2)
 if not intp%5:
  value.append(p)
print (','.join(value))
