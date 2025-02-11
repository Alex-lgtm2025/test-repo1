
print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
p = (a + b + c) / 2
s = treu(p * (p - a) * (p - b) * (p - c))
print("Площадь: %.2f" % s)
 