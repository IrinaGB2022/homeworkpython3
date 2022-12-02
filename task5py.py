ax = float(input('Kоординаты точки a по оси x:'))
ay = float(input('Kоординаты точки a по оси y:'))
bx = float(input('Kоординаты точки b по оси x:'))
by = float(input('Kоординаты точки b по оси y:'))

import math
dist= math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {dist}' )