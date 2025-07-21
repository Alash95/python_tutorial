"""Writeaprogramthatgeneratesarandomdecimalnumberbetween1and10withtwodecimal
 places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00."""

import random
import decimal

x = float(random.randrange(100, 1000))/100
print(f"thr random number is: {x}")