# Manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')

print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')

print(f'Infinito negativo: {infinito_negativo}')

print(f'Es infinito?: {math.isinf(infinito_negativo)}')

infinito_positivo = 0
infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')

print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = 0
infinito_negativo = -math.inf

print(f'Infinito negativo: {infinito_negativo}')

print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# Usando la libreria decimal

inf_positivo = Decimal('Infinity')

print(f'Infinito positivo: {inf_positivo}')

print(f'Es infinito?: {math.isinf(inf_positivo)}')


inf_negativo = Decimal('-Infinity')

print(f'Infinito negativo: {inf_negativo}')

print(f'Es infinito?: {math.isinf(inf_negativo)}')