
print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))**0.5
print("Площадь: %.2f" % s)
 