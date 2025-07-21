# from CodeWithMosh.Modules_.ecommerce.shopping.sales import calc_shipping, calc_tax
# import CodeWithMosh.Modules_.ecommerce.shopping.sales as sales
# from CodeWithMosh.Modules_.ecommerce.shopping import sales
# import sys

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modules_.ecommerce.shopping import sales

# Print the available attributes in the sales module
# print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)


# print(sys.path)
# print(dir(sales))

# sales.calc_tax()


# calc_shipping()
# calc_tax()
