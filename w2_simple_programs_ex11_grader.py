'''
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25 * n * s^2) / tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
'''

import math

def polysum(n, s):
    
    def perimeter(n, s):
        if s == 1:
            return n
        return n + perimeter(n, (s - 1))
        
    def area(n, s):
        numerator = (0.25 * n) * (s**2)
        denominator = math.tan(math.pi / n)
        return numerator / denominator
        
    return round((perimeter(n, s) ** 2) + area(n, s), 4)
        
print(polysum(13, 82))