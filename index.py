from ecommerce.shopping.sales import  calc_shipping,calc_tax;
from ecommerce.shopping import sales
import sys;

calc_shipping();
calc_tax();

sales.calc_tax();
sales.calc_shipping();

print(sys.path)

for path in sys.path:
    print(path)