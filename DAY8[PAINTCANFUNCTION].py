#assumed one can of paint covers 5 square meters
#cannot buy partial cans of paint

import math
def paint_calc (height, width):
    area = int(height) * int(width)
    cans = (area/5)
    result = math.ceil(cans)
    print(f"you will need {result} cans of paint")

paint_calc(3,2)