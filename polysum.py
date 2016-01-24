from math import pi, tan

""" 
Sum the area and square of the perimter of a regular polygon 
rounded to 4 decimal places.
"""

def polysum(n, s):

    def area_polygon(n, s):
        return (0.25 * n * s ** 2) / tan(pi/n) 
    
    def perimeter_polygon(n, s):
        return n * s
        
    area = area_polygon(n, s)
    perimeter_squared = perimeter_polygon(n, s) ** 2
    
    # convert to string for the four decimals places then to int
    return float(str(format(area + perimeter_squared, '.4f')))
    