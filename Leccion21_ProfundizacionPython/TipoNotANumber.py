# NaN, NAN, nan, nAn, Nan, naN, nAN: significa Not a Number, no es sensible a mayusculas
# Es un tipo de dato númerico indefinido
import math
from decimal import Decimal

a = float('NaN')
print(f'a: {a}')

print(f'Es Nan?: {math.isnan(a)}')

# Con Decimal
a = Decimal('NaN')

print(f'a: {a}')

print(f'Es Nan?: {math.isnan(a)}')